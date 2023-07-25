import arcade

import SnaKee
from Modules.BaseLevel import Level as BaseLevel
from Utilities.WindowManager import WindowManager


class Level(BaseLevel):
    levelName = "LEVEL NOPE"

    sHeight = 500
    sWidth = 500
    sMaxWidth = 1500
    sMaxHeight = 800
    sMinWidth = 200
    sMinHeight = 200

    sPositionX = 750
    sPositionY = 250

    isFixedBG = True
    #backgroundImagePath = ":resources:images/tiles/sandCenter.png"
    backgroundImagePath = ":resources:images/tiles/sandCenter.png"

    def __init__(self, window: arcade.Window):
        super().__init__(window)
        #self.NextLevel = Levels.Level1


    def LevelFunctionality(self):
        super().LevelFunctionality()

        # DO CONSTANT THINGS ON UPDATE

    def SetupLevelWindow(self):
        #self.window.UnlockWindow()
        super().SetupLevelWindow()

        self.winManager.SetWindowCaption(self.levelName)
        pass

    def GenerateLevelObjects(self):
        super().GenerateLevelObjects()
        pass

    def GenerateLevel(self):
        super().GenerateLevel()
        pass

    def ResizeLevel(self, width, height):
        super().ResizeLevel(width, height)

        if (not self.winManager.isWidthLocked) and self.winManager.sCurrWidth > 900:
            self.winManager.SelectWindowLock("width", 900)

        if (not self.winManager.isHeightLocked) and self.winManager.sCurrHeight < 250:
            self.winManager.SelectWindowLock("height", 250)


        self.winManager.SetWindowCaption(f"Window size: {self.winManager.sCurrWidth} x {self.winManager.sCurrHeight}")
