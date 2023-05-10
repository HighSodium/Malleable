from SnaKee import arc

class Player(object):
    positionX = 10
    positionY = 10
    character_scale = 1.0
    sprite = [":resources:images/tiles/boxCrate.png",
              ":resources:images/tiles/boxCrate_single.png",
              ":resources:images/tiles/boxCrate_double.png"]


    def __init__(self, posX, posY):
        self.playerSprite = arc.Sprite(self.sprite[2], self.character_scale)
    

    def set_position(self, x, y):
        self.playerSprite.center





