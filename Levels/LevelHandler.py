from Levels import *
from Levels import BaseLevel, Level0


class LevelHandler(object):




    def __init__(self):
        activeLevel = Level0.Level()



    def LoadFromBeginning(self):
        pass

    def LoadLevelSpecific(self, level: BaseLevel):
        print(level.name)




