#!/usr/bin/env
__all__ = ["interactive_binsearch", "get_next_positions", "getmiddle_pos_and_value"]

# Add current directory to syspath
from dataclasses import dataclass
from pathlib import Path

cdir = Path(__file__).parent
from sys import path as syspath

if str(cdir) not in syspath:
    syspath.append(str(cdir))

from readdata import readValueData
from random import randrange
from configuration import saveConfig, config

cf = config["general"]
MAX_POSITION_ALLOWED = int(cf["MAX_POSITION_ALLOWED"])
MAX_TRIES = int(cf["MAX_TRIES"])


@dataclass
class Response:
    found: bool
    initpos: int
    endpos: int
    middlepos: int
    curr_try: int


def _getmiddle(initpos: int, endpos: int) -> int:
    """Identify middle position and value of a giver list of values

    Args:
        initpos (int): initial position _ lower value
        endpos (int):  end position_ max value

    Returns:
        middlepos (int) : middle position
    """
    middlepos = (initpos + endpos) // 2
    return middlepos


def getmiddle_pos_and_value(
    initpos: int = 1, endpos: int = MAX_POSITION_ALLOWED
) -> int:
    """reads the middlepos and value

    Args:
        values: iterator with values shorted

    Returns:
        middlepos (int), middlevalue (unknown type)
    """

    if endpos > MAX_POSITION_ALLOWED:
        raise ValueError(f"Maximum value allowed {MAX_POSITION_ALLOWED}")

    if initpos > endpos:
        raise ValueError(
            f"Initpos {initpos} values must be lesser than end value {endpos}"
        )

    middlepos = _getmiddle(initpos, endpos)
    middlevalue = readValueData(middlepos)
    return (middlepos, middlevalue)


def get_next_positions(
    condition: bool, selectedpos: int, initpos: int, endpos: int
) -> int:
    """Return next positions

    Args:
        condition (bool): _description_
        selectedpos (int): selected position to search
        initpos (int): initial position
        endpos (int): end position


    Returns:
        dict{initpos:int, endpos:int}: dictionary with next selected positions
    """
    if condition:
        return {"initpos": selectedpos + 1, "endpos": endpos}
    else:
        return {"initpos": initpos, "endpos": selectedpos}


def interactive_binsearch(
    curr_try: int,
    conditionEvaluator=lambda x: True,
    initpos: int = 0,
    endpos: int = MAX_POSITION_ALLOWED,
    **kwargs,
) -> Response:
    """Interactively move trow every step of the binary search waiting for user response
    or not asynchronous condition evaluator

    Args:
        curr_try (int): try number
        conditionEvaluator (_type_, optional): function to get a value or a boolean. Defaults to lambdax:True.
        initpos (int, optional): initial position durent current iteration. Defaults to 0.
        endpos (int, optional): final position durent current iteration. Defaults to MAX_POSITION_ALLOWED.

    Returns:
        Response object
    """
    middlepos = _getmiddle(initpos, endpos)
    res = get_next_positions(conditionEvaluator(), middlepos, initpos, endpos)
    if middlepos in (endpos, initpos):
        middlepos = [initpos, endpos][conditionEvaluator()]
        return Response(True, initpos, endpos, middlepos, curr_try + 1)
    if curr_try > MAX_TRIES:
        return Response(False, initpos, endpos, middlepos, curr_try + 1)
    initpos, endpos = res["initpos"], res["endpos"]
    return Response(False, initpos, endpos, _getmiddle(initpos, endpos), curr_try + 1)
