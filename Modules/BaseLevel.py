# import random
# import time
import arcade
from Utilities.WindowManager import WindowManager

class Level:
    """An instance of a level containing information for the level setup"""

    # -------- Level Info ---------
    levelName = "Default Name"
    showLockLine = True

    # -------- Background Info ---------
    isFixedBG = True
    backgroundImagePath: str = None
    backgroundImage: arcade.Texture = None
    backgroundColor: arcade.Color = arcade.color.SKY_BLUE

    # -------- Screen Info ---------
    sWidth = 500
    sHeight = 500
    sMaxWidth = 750
    sMaxHeight = 750
    sMinWidth = 100
    sMinHeight = 150

    sPositionX = 750
    sPositionY = 250
    # -------- object ---------
    dynamicObjects = []
    physicsObjects = []
    staticObjects = []
    collectables = []
    effectors = []
    # -------- player info ---------
    players = []
    playerSpawnLocationList: list[int, int] = [0, 0]
    playerSpawnLocation: list[int, int] = [0, 0]

    winManager: WindowManager = None
    gameWindow: arcade.Window = None

    def __init__(self, window: arcade.Window):
        self.gameWindow = window
        self.winManager = window.windowManager

        #--- Load Textures ---
        if self.backgroundImagePath is not None:
            self.backgroundImage = arcade.load_texture(self.backgroundImagePath)

        pass

# --------------- LEVEL GENERATION -----------------------------------
    def LevelFunctionality(self):
        """The game loop for the level"""
        pass

    def DrawLevel(self):
        # -------- Draw Background --------
        if self.backgroundImagePath is not None:
            if self.isFixedBG:
                w = self.sMaxWidth
                h = self.sMaxHeight
                originH = self.winManager.sCurrHeight - self.sMaxHeight
            else:
                w = self.winManager.sCurrWidth
                h = self.winManager.sCurrHeight
                originH = 0
            arcade.draw_lrwh_rectangle_textured(0, originH, w, h, self.backgroundImage)


        if self.showLockLine:
            pointListTB = ((0, 0), (self.sMaxWidth, 0),
                           (0, self.winManager.sCurrHeight), (self.sMaxWidth, self.winManager.sCurrHeight))
            pointListLR = ((0, 0), (0,self.sMaxHeight),
                           (self.winManager.sCurrWidth, 0), (self.winManager.sCurrWidth, self.sMaxHeight))
            arcade.draw_lines(pointListTB, arcade.color.RED if self.winManager.isHeightLocked else arcade.color.GREEN, 4)
            arcade.draw_lines(pointListLR, arcade.color.RED if self.winManager.isWidthLocked else arcade.color.GREEN, 4)


    def SetupLevelWindow(self):
        """Use this method to set up the gameplay window parameters"""
        self.winManager.SetWindowSize(self.sWidth, self.sHeight)
        self.winManager.SetWindowMaxSize(self.sMaxWidth, self.sMaxHeight)
        self.winManager.SetWindowMinSize(self.sMinWidth, self.sMinHeight)
        self.winManager.SetWindowPosition(self.sPositionX, self.sPositionY)
        arcade.set_background_color(self.backgroundColor)

        pass

    def GenerateLevelObjects(self):
        """Use this method to generate the objects in a level"""
        self.GeneratePhysicsObjects()
        self.GenerateStaticObjects()
        self.GenerateDynamicObjects()
        self.GenerateCollectableObjects()
        pass

    def GenerateStaticObjects(self):
        """Use this method to generate the immovable objects in a level"""
        pass

    def GenerateDynamicObjects(self):
        """Use this method to generate the scripted moving objects in a level"""
        pass

    def GeneratePhysicsObjects(self):
        """Use this method to generate the physics objects in a level"""
        pass

    def GenerateCollectableObjects(self):
        """Use this method to generate anything that can be collected in a level"""
        pass


    def GenerateLevel(self):
        """This method is the final call for generation"""
        self.SetupLevelWindow()
        self.GenerateLevelObjects()
        pass

    #----------------- END LEVEL GENERATION ------------------------------

    # def GetRandomSpawnLocation(self):
    #     for loc in self.playerSpawnLocationList:
    #         random.seed(time.time())
    #         return random.randint(0, len(self.playerSpawnLocationList) - 1)
    #         #fix spawn location to access random index

    def GetCurrentSpawnLocation(self):
        return self.playerSpawnLocation


    def ResizeLevel(self, width, height):
        arcade.set_viewport(0, self.winManager.sCurrWidth, 0, self.winManager.sCurrHeight)
        self.sWidth = width
        self.sHeight = height
        self.winManager.UpdateSize(width, height)
        pass


# holders for next and previous level links
NextLevel: Level
PrevLevel: Level
