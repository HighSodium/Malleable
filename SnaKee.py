import arcade
#from Modules.BaseLevel import Level
from Utilities.WindowManager import WindowManager
from Utilities.LevelManager import LevelManager
from Utilities.InputManager import InputManager


#TODO: Idea: We're using the literal window to shake around a ball/object


class SnaKee(arcade.Window):
    currentLevelNumber = 0
    windowManager: WindowManager
    #currentLevel: Level

    def __init__(self, resize):
        super().__init__(resizable=resize)
        self.windowManager = WindowManager(self)
        self.levelManager = LevelManager(self)
        self.inputManager = InputManager(self)
        print(SnaKee.currentLevelNumber)


    def setup(self):
        """ USE THIS TO RESTART THE GAME """
        self.levelManager.LoadLevelByNumber(self.currentLevelNumber)

        #self.physicsEngine = arcade.PhysicsEngineSimple()

    def on_resize(self, width, height):
        #super().on_resize(width, height)
        self.windowManager.UpdateSize(width, height)
        self.levelManager.currentLevel.ResizeLevel(width, height)


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        #super().on_mouse_release(x, y, button, modifiers)
        #currentLevelNumber += 1
        #self.setup()
        pass

    # def on_key_press(self, symbol: int, modifiers: int):
    #     if playerController is not None:
    #         pass


    def on_draw(self):
        self.clear()
        self.levelManager.currentLevel.DrawLevel()
        # vvvv CODE TO DRAW GOES HERE vvvv

    def on_update(self, delta_time: float):
        self.levelManager.currentLevel.LevelFunctionality()




#------------------------------------------------------------------
##### THIS IS THE GAME ######
def main():

    # TODO (LOW): Get rid of the resizeable setup and make # it part of the level somehow
    game = SnaKee(True)
    game.setup()
    game.run()


if __name__ == "__main__":
    main()

