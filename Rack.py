## Third module implemented for the HAZMAT A-math solver - manages rack dynamics.
## Each game of A-Math will contain two rack objects (although, no reason not to allow more for multiplayer games).
## The rules of A-Math dictate that racks should contain 8 tiles at all times if possible.

## Currently implemented functions

from Tile import Tile
from Tilebag import Tilebag

class Rack:
    
    tile_limit = 8 #could change to 7 to make more similar to Scrabble!
    
    def __init__(self):
        
        self.tiles_on_rack = []  #will be filled with Tile objects by a Game
        
        
    ## default: Fill rack back up to 8 tiles from Tilebag object tb
    def fill_rack(self, tb):
        draw_how_many_tiles = min(Rack.tile_limit - len(self.tiles_on_rack), tb.how_many_in_bag())
        [ self.tiles_on_rack.append(tb.draw_tile()) for i in range(draw_how_many_tiles) ]
        
        
    ## set rack to input letters.
    def set_rack_to_input(self, current_tilebag):
        return 1
    
    
    ## print out tiles on rack nicely and in some order of choice.
    def print_tiles_on_rack(self):
        return 2