#!/usr/bin/env
from readdata import readValueData
from random import randrange
from configuration import saveConfig, config

if config is None:
    MAX_POSITION_ALLOWED = 61695
    MAX_TRIES = 16
else:
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
        return {"initpos": selectedpos + 1, "endpos": endpos}
    else:
        return {"initpos": initpos, "endpos": selectedpos}


def test():
    print("Think a value beetween 1 and 61961")
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)
    print("press 1 if true else any value")
    tryes = 0
    maxtryes = MAX_TRIES
    while True:
        tryes += 1
        condition = input(f"[Try {tryes}] is the value greater than {middlevalue}?")
        res = get_next_positions(condition == "1", middlepos, initpos, endpos)

        # Stop condition
        if endpos == middlepos or initpos == middlepos:
            middlevalue = [initpos, endpos][condition == "1"]
            print(f"Encontrado: {middlevalue} tries {tryes}")
            return
        if tryes > maxtryes + 1:
            print("No encontrado")
            return selectecValue, middlevalue, tryes

        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)


def auto_test():
    selectecValue = randrange(500, MAX_POSITION_ALLOWED - 1000)
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)
    tryes = 0
    maxtryes = 16
    while True:
        tryes += 1
        condition = [0, "1"][selectecValue > middlevalue]
        res = get_next_positions(condition == "1", middlepos, initpos, endpos)
        if endpos == middlepos or initpos == middlepos:
            return selectecValue, [initpos, endpos][condition == "1"], tryes
        if tryes > maxtryes + 1:
            return selectecValue, middlevalue, tryes
        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = _getmiddle_pos_and_value(initpos, endpos)


if __name__ == "__main__":
    test()
    buenos = 0
    for i in range(1000):
        selectecValue, middlevalue, tryes = auto_test()
        if selectecValue != middlevalue:
            print(f"{selectecValue}: {middlevalue} tries {tryes}")
        else:
            buenos += 1
    print(f"Resultados exitosos {buenos}")
