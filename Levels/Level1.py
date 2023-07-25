import arcade
from Modules.BaseLevel import Level as BaseLevel


class Level(BaseLevel):
    levelName = "Folded"

    

    def ResizeLevel(self, width, height):
        super().ResizeLevel(width, height)
        self.winManager.SetWindowCaption("FUCK YOU! BOOM!")

    def LevelFunctionality(self):
        super().LevelFunctionality()
        # DO CONSTANT THINGS ON DRAW


