## Third module implemented for the HAZMAT A-math solver - manages rack dynamics.
## Each game of A-Math will contain two rack objects (although, no reason not to allow more for multiplayer games).
## The rules of A-Math dictate that racks should contain 8 tiles at all times if possible.

from Tile import Tile
from Tilebag import Tilebag

class Rack:
    
    def __init__(self):
        
        self.tiles_on_rack = []  #will be filled with Tile objects by a Game
        
        
    ## default: Fill rack back up to 8 tiles.
    def fill_rack(self, current_tilebag):
        return 0
        
    ## set rack to input letters.
    def set_rack_to_input(self, current_tilebag):
        return 1
