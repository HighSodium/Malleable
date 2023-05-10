from SnaKee import arc
from SnaKee import SCR_HGHT
from SnaKee import SCR_WDTH

currWinSizeX = 500
currWinSizeY = 500
windowSizeLocked = False

def __init__():
    UpdateSize(SCR_HGHT, SCR_WDTH)


def CheckSize(width, height):
    curX = currWinSizeX
    curY = currWinSizeY
    check = (curX == width and curY == height)
    return check


def UpdateSize(width: int, height: int):
    if not CheckSize(width, height):
        global currWinSizeX
        global currWinSizeY
        currWinSizeX = width
        currWinSizeY = height
        #print(f"You sized the window to {width} x {height}! Good job!")



def UpdateSizeTuple(sizeTuple):
    if not CheckSize(sizeTuple[0], sizeTuple[1]):
        x = currWinSizeX.append(sizeTuple[0])
        y = currWinSizeY.append(sizeTuple[1])
        #print(f"You sized the window to {x} x {y}! Good job!")










