import pytest
from backend.binarysearch import (
    get_next_positions,
    getmiddle_pos_and_value,
    interactive_binsearch,
)
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
    while True:
        tryes += 1
        condition = selectecValue > middlevalue
        res = get_next_positions(condition, middlepos, initpos, endpos)
        if middlepos in (initpos, endpos):
            middlepos = [initpos, endpos][condition]
            middlevalue = readValueData(middlepos)
            assert selectecValue == middlevalue
            break
        if tryes > MAX_TRIES + 1:
            assert tryes <= MAX_TRIES
            break
        initpos, endpos = res["initpos"], res["endpos"]
        middlepos, middlevalue = getmiddle_pos_and_value(initpos, endpos)


def test_interactive_binsearch():
    selectecValue = randrange(MAX_POSITION_ALLOWED)
    initpos = 0
    endpos = MAX_POSITION_ALLOWED
    _, middlevalue = getmiddle_pos_and_value(initpos, endpos)

    tryes = 0
    while True:
        tryes += 1
        condition = selectecValue > middlevalue
        res = interactive_binsearch(tryes, lambda: condition, initpos, endpos)
        if res.found:
            print(res.curr_try)
            middlevalue = readValueData(res.middlepos)
            assert selectecValue == middlevalue
            return
        if res.curr_try > MAX_TRIES + 1:
            assert res.curr_try <= MAX_TRIES
            break
        initpos = res.initpos
        endpos = res.endpos
        middlevalue = readValueData(res.middlepos)
