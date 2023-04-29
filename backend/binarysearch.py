#!/usr/bin/env
from readdata import readValueData

MAX_POSITION_ALLOWED = 61696 - 1


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


def _getmiddlevalue(initpos: int = 1, endpos: int = MAX_POSITION_ALLOWED) -> int:
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


def get_next(contidition: bool, initpos: int, endpos: int, middlepos: int) -> int:
    if not contidition:
        return {initpos: middlepos, endpos: endpos}
    else:
        return {initpos: initpos, endpos: middlepos}


if __name__ == "__main__":
    pass
