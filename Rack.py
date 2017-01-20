## Third module implemented for the HAZMAT A-math solver - manages rack dynamics.
## Each game of A-Math will contain two rack objects (although, no reason not to allow more for multiplayer games).
## The rules of A-Math dictate that racks should contain 8 tiles at all times if possible.

## Currently implemented functions:
##    -exchange_tiles: after verifying that desired exchange is illegal, uses swap_tiles function from Tilebag to replace
##       selected tiles with random tiles from bag.
##    -fill_rack: fill rack back to maximum length tile_limit from Tilebag tb
##    -print_tiles_on_rack: Print out all of the tiles currently on a given rack.
##    -set_rack_to_input: manually change rack to listed input.

from Tile import Tile
from Tilebag import Tilebag

class Rack:
    
    tile_limit = 8 #could change to 7 to make more similar to Scrabble!
    
    def __init__(self):
        self.tiles_on_rack = []  #will be filled with Tile objects by a Game calling function fill_rack.
        
        
    ## default: Fill rack back up to 8 tiles from Tilebag object tb
    ## is this the right way of doing this? currently not returning tilebag object, but editing in place.
    def fill_rack(self, tb):
        draw_how_many_tiles = min(Rack.tile_limit - len(self.tiles_on_rack), tb.how_many_in_bag())
        [ self.tiles_on_rack.append(tb.draw_tile()) for i in range(draw_how_many_tiles) ]
        
        
    ## set rack to input letters, with desired letters delimited by commas.
    def set_rack_to_input(self, tb, rack):
        
        # design function to accept either spaces or commas to separate input.
        desired_rack = [ x.strip() for x in rack.replace(',',' ').split(' ') ]
        
        if len(desired_rack) > 8:
            print('Requested rack with over 8 tiles - are you sure?')
            override = input('Are you sure you want to continue? (n)o or (y)es:')
                  
            if override.lower() not in ['y', 'yes']:
                print('Did not adjust rack.')
                return

        #[ tb.add_tile_to_bag(old_tile.pot) for old_tile in self.tiles_on_rack ]  ## 
        #[ self.tiles_on_rack.append(tb.draw_tile(new_tile)) for new_tile in desired_rack ]

                  
    ## print out tiles on rack nicely and in some order of choice.
    def print_tiles_on_rack(self):
        print(' '.join([ x.pot for x in self.tiles_on_rack ]))
    
    def exchange_tiles(self, tb):
        return 3