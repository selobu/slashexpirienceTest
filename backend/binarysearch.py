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
    middlepos = (initpos + endpos) // 2 + 1
    return middlepos


def _getmiddle_pos_and_value(
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
        if selectedpos == endpos + 1:
            return {"initpos": endpos, "endpos": endpos}
        return {"initpos": selectedpos, "endpos": endpos}
    else:
        if selectedpos == endpos + 1:
            return {"initpos": initpos, "endpos": initpos}
        return {"initpos": initpos, "endpos": selectedpos}


def test():
    print("Think a value beetween 1 and 61961")
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)
    print("press 1 if true else any value")
    tryes = 0
    while True:
        tryes += 1
        condition = input(f"[Try {tryes}] is the value greater than {middlevalue}?")
        res = get_next_positions(condition == "1", middlepos, initpos, endpos)
        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)
        if initpos == middlepos or endpos == middlepos:
            print(f"Encontrado: {middlepos} tries {tryes}")
            return


if __name__ == "__main__":
    test()
