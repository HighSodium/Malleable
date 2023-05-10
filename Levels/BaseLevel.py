import random
import time
from SnaKee import arc

class BaseLevel(object):
    """An instance of a level containing information for the level setup"""
    name = "Default Level"    
    backgroundImage: str
    # -------- object ---------
    dynamicObjects = []
    physicsObjects = []
    staticObjects = []
    collectables = []
    effectors = []
    # -------- player info ---------
    players = []
    player_spawn_locations: list[int, int] = {0, 0}
    # -------- Level Info --------
    # TODO: oaiweoaijoia


    def __init__(self):
        self.player_spawn_locations = [0, 0]
        pass

    def setup(self):
        pass


    def get_spawn_location(self):
        for loc in self.player_spawn_locations:
            random.seed(time.time())
            return random.randint(0, len(self.player_spawn_locations) - 1)
            # TODO: fix spawn location to access random index
    

prevLevel: BaseLevel()
nextLevel: BaseLevel()

