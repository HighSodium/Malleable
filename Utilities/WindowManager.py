import arcade
from enum import Enum
from typing import Literal

class WindowManager(object):

    sCurrWidth = 500
    sCurrHeight = 500
    currWindowPosX = 500
    currWindowPosY = 500
    isWidthLocked = False
    isHeightLocked = False


    def __init__(self, window: arcade.Window):
        self.gameWindow = window



    def CheckSize(self, width: int, height: int):
        curX = self.sCurrWidth
        curY = self.sCurrHeight
        isSameSize = (curX == width and curY == height)
        return isSameSize

    def UpdateSize(self, width: int, height: int):
        if not self.CheckSize(width, height):
            self.sCurrWidth, self.sCurrHeight = self.gameWindow.get_size()
            #self.sCurrHeight = self.gameWindow.get_size()[1]
            #print(f"You sized the window to {width} x {height}! Good job!")


    def UpdateSizeTuple(self, sizeTuple):
        if not self.CheckSize(sizeTuple[0], sizeTuple[1]):
            x = self.sCurrWidth.append(sizeTuple[0])
            y = self.sCurrHeight.append(sizeTuple[1])
            #print(f"You sized the window to {x} x {y}! Good job!")

    def SetWindowSize(self, width, height):
        self.gameWindow.set_size(width, height)
        self.UpdateSize(width, height)

    def SetWindowWidth(self, width):
        self.gameWindow.set_size(width, self.sCurrHeight)
        self.UpdateSize(width, self.sCurrHeight)

    def SetWindowHeight(self, height):
        self.gameWindow.set_size(self.sCurrWidth, height)
        self.UpdateSize(self.sCurrWidth, height)


    def SelectWindowLock(self, select: Literal["width", "height", "both"], lockValue):
        currLevel = self.gameWindow.levelManager.currentLevel
        match select:
            case "width":
                self.isWidthLocked = True
                self.SetWindowMinSize(lockValue, self.sCurrHeight if self.isHeightLocked else currLevel.sMinHeight)
                self.SetWindowMaxSize(lockValue, self.sCurrHeight if self.isHeightLocked else currLevel.sMaxHeight)

            case "height":
                self.isHeightLocked = True
                self.SetWindowMinSize(self.sCurrWidth if self.isWidthLocked else currLevel.sMinWidth, lockValue)
                self.SetWindowMaxSize(self.sCurrWidth if self.isWidthLocked else currLevel.sMaxWidth, lockValue)
            case "both":
                self.SetWindowMinSize(lockValue, lockValue)
                self.SetWindowMaxSize(lockValue, lockValue)
            case _:
                raise ValueError("Not a valid argument (width, height, both)")
                pass

        self.UpdateSize(self.sCurrWidth, self.sCurrHeight)
        pass




    def LockWindowSize(self, width, height):
        self.SetWindowSize(self.sCurrWidth, self.sCurrHeight)
        self.gameWindow.set_maximum_size(self.sCurrWidth, self.sCurrHeight)
        self.gameWindow.set_minimum_size(self.sCurrWidth, self.sCurrHeight)
        self.UpdateSize(width, height)




    def UnlockWindow(self):
        """Unlock the window to a maximum and a minimum"""
        currWindow = self.gameWindow.levelManager.currentLevel
        self.isHeightLocked = False
        self.isWidthLocked = False
        self.gameWindow.set_maximum_size(currWindow.sMaxWidth, currWindow.sMaxHeight)
        self.gameWindow.set_minimum_size(currWindow.sMinWidth, currWindow.sMinHeight)


    def SetWindowMinSize(self, minWidth, minHeight):
        #DO MINIMUM SIZE THINGS
        self.gameWindow.set_minimum_size(minWidth, minHeight)

    def SetWindowMaxSize(self, maxWidth, maxHeight):
        #DO MAXIMUM SIZE THINGS
        self.gameWindow.set_maximum_size(maxWidth, maxHeight)

    def SetWindowCaption(self, title):
        self.gameWindow.set_caption(title)

    def SetWindowPosition(self, sPosX, sPosY):
        print(sPosX, sPosY)
        self.gameWindow.set_location(sPosX, sPosY)
        print(self.gameWindow.get_location())
        pass


