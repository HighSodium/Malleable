import arcade as arc
from Utilities import WinSizer
from Levels import LevelHandler as LH

SCR_WDTH = 1000
SCR_HGHT = 500
SCR_TITL = "SnaKee"
#TODO: Idea change: We're using the literal window to shake around a ball/object

class SnaKee(arc.Window):
    Manager = LH.LevelHandler()

    def __init__(self, sWidth, sHeight, title, resize):
        super().__init__(sWidth, sHeight, title, resizable=resize)
        arc.Window.set_maximum_size(self, 1500, 750)
        arc.Window.set_minimum_size(self, 200, 200)
        arc.set_background_color(arc.csscolor.MAROON)



    def setup(self):
        """ USE THIS TO RESTART THE GAME """
        Manager.LoadLevelSpecific(Levels.Level0)


    def on_resize(self, width, height):
        super().on_resize(width, height)
        # size = arc.Window.get_size(self)
        WinSizer.UpdateSize(width, height)
        arc.Window.set_caption(self, f"Window size: {WinSizer.currWinSizeX} x {WinSizer.currWinSizeY}")


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        super().on_mouse_release(x, y, button, modifiers)


    def on_draw(self):
        self.clear()
        # vvvv CODE TO DRAW GOES HERE vvvv

def main():

    game = SnaKee(SCR_WDTH, SCR_HGHT, SCR_TITL, True)
    game.setup()
    game.run()


if __name__ == "__main__":
    main()

