import pytest
from backend.binarysearch import get_next_positions, getmiddle_pos_and_value
from backend.readdata import readValueData
from backend.configuration import config
from random import randrange

cf = config["general"]
MAX_POSITION_ALLOWED = int(cf["MAX_POSITION_ALLOWED"])
MAX_TRIES = int(cf["MAX_TRIES"])


def test_binary():
    """Auto test random value"""
    selectecValue = randrange(MAX_POSITION_ALLOWED)
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    middlepos, middlevalue = getmiddle_pos_and_value(initpos, endpos)
    tryes = 0
    maxtryes = MAX_TRIES
    while True:
        tryes += 1
        condition = [0, "1"][selectecValue > middlevalue]
        res = get_next_positions(condition == "1", middlepos, initpos, endpos)
        if endpos == middlepos or initpos == middlepos:
            middlepos = [initpos, endpos][condition == "1"]
            middlevalue = readValueData(middlepos)
            assert selectecValue == middlevalue
            break
        if tryes > maxtryes + 1:
            assert tryes <= maxtryes
            break
        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = getmiddle_pos_and_value(initpos, endpos)
