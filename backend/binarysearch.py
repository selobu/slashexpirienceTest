#!/usr/bin/env
__all__ = ["get_next_positions", "getmiddle_pos_and_value"]

from readdata import readValueData
from random import randrange
from configuration import saveConfig, config

cf = config["general"]
MAX_POSITION_ALLOWED = int(cf["MAX_POSITION_ALLOWED"])
MAX_TRIES = int(cf["MAX_TRIES"])


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


def test():
    """Test a single value"""
    print("Think a value beetween 1 and 61961")
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    middlepos, middlevalue = getmiddle_pos_and_value(initpos, endpos)
    print("press 1 if true else any value")
    tryes = 0
    maxtryes = MAX_TRIES
    while True:
        tryes += 1
        condition = input(f"[Try {tryes}] is the value greater than {middlevalue}?")
        res = get_next_positions(condition == "1", middlepos, initpos, endpos)

        # Stop conditions
        if endpos == middlepos or initpos == middlepos:
            middlepos = [initpos, endpos][condition == "1"]
            middlevalue = readValueData(middlepos)
            print(f"Found: {middlevalue} tries {tryes}")
            return
        if tryes > maxtryes + 1:
            print("Not found")
            return selectecValue, middlevalue, tryes

        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)


if __name__ == "__main__":
    # test()
    well_caclulated = 0
    for i in range(200):
        selectecValue = randrange(MAX_POSITION_ALLOWED)
        selectecValue, middlevalue, tryes = auto_test(selectecValue)
        if selectecValue != middlevalue:
            print(f"{selectecValue}: {middlevalue} tries {tryes}")
        else:
            well_caclulated += 1
    print(f"Successfull results {well_caclulated}")
