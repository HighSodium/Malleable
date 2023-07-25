import arcade


class InputManager(object):
    #TODO: (NEXT) GET INPUTS WORKING!

    def __init__(self, window: arcade.Window):
        ## --------- State initial inputs ---------
        self.inputUp = arcade.key.W
        self.inputDown = arcade.key.S
        self.inputLeft = arcade.key.A
        self.inputRight = arcade.key.D
        self.inputJump = arcade.key.SPACE
        self.inputDash = arcade.key.LSHIFT
        self.inputGrapple = arcade.key.LSHIFT
        self.inputLeftMouse = arcade.MOUSE_BUTTON_LEFT
        self.inputRightMouse = arcade.MOUSE_BUTTON_RIGHT

        self.game = window
        pass


    def on_input(self, input):


        pass






