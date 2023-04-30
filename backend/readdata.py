# connect data with api

tempvalues = list(range(250, 61696 + 1))


def readValueData(pos: int):
    """Reads the value at a given position

    Args:
        pos (int): postition to get the value data
    """
    return tempvalues[pos]
