import arcade
from Modules.BaseLevel import Level
from Utilities.WindowManager import WindowManager
#from Levels import Level0, Level1

class LevelManager(object):

    currentLevel: Level

    def __init__(self, window: arcade.Window):
        self.gameWindow = window
        currentLevel: Level
        pass

    @classmethod
    def PreloadLevel(cls, levelNum):
        """Load the level from file before calling its attributes"""
        import importlib.util
        import sys
        #import os, os.path

        #print(len([name for name in os.listdir(os.getcwd() + "/Levels")]) - 1)


        spec = importlib.util.spec_from_file_location("Level"+str(levelNum), "Levels\\Level" + str(levelNum) + ".py")
        foo = importlib.util.module_from_spec(spec)
        sys.modules["Level"+str(levelNum)] = foo
        spec.loader.exec_module(foo)
        return foo

    def LoadFromBeginning(self):
        pass

    def LoadLevelSpecific(self, level: Level):
        #self.PreloadLevel()
        print(level.levelName)


    def LoadLevelByNumber(self, levelNum: int):
        loadedLevel = self.PreloadLevel(levelNum)
        #print(loadedLevel.Level.levelName)

        #TODO: Move this to another function to allow for additional functionality
        self.currentLevel = loadedLevel.Level(self.gameWindow)
        self.currentLevel.GenerateLevel()
        #find an instance of LEVEL






