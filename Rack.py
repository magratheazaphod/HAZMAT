## Third module implemented for the HAZMAT A-math solver - manages rack dynamics.
## Each game of A-Math will contain two rack objects (although, no reason not to allow more for multiplayer games).
## The rules of A-Math dictate that racks should contain 8 tiles at all times if possible.

## Currently implemented functions:
##    -exchange_tiles: after verifying that desired exchange is illegal, uses swap_tiles function from Tilebag to replace
##       selected tiles with random tiles from bag.
##    -fill_rack: fill rack back to maximum length tile_limit from Tilebag tb
##    -print_tiles_on_rack: Print out all of the tiles currently on a given rack.
##    -set_rack_to_input: manually change rack to listed input.

## ONGOING PROBLEMS:
## 1) The tiles that you want might be on the other players rack - have to be able to check for that case.

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
        
        # accept either spaces or commas to separate input.
        desired_rack = [ x.strip() for x in rack.replace(',',' ').split(' ') ]
        
        if len(desired_rack) > 8:
            print('Requested rack with over 8 tiles - are you sure?')
            override = input('Are you sure you want to continue? (n)o or (y)es:')
                  
            if override.lower() not in ['y', 'yes']:
                print('Did not adjust rack.')
                return

        #[ tb.add_tile_to_bag(old_tile.pot) for old_tile in self.tiles_on_rack ]  ## 
        #[ self.tiles_on_rack.append(tb.draw_tile(new_tile)) for new_tile in desired_rack ]
        

    # very similar to draw_tile module, except that we require a definite input of what tiles are being removed
    # in contrast, in the tilebag class it's important to have a random draw option.
    # other slight difference is that draw_tile returns one tile at a time, while here we do a bunch at once.
    def remove_tiles_from_rack(self, tiles_desired):
        
        removed_tiles = []
        
        for nexttile in tiles_desired:
            removed_tiles.append(self.remove_single_tile(nexttile))
       
        return removed_tiles
    
    ##called above my remove_tiles_from_rack, removes a single tile from rack object.
    ##spits out the tile that was just removed from the rack.
    def remove_single_tile(self, tile_desired):
        
        #if we try to draw a tile that doesn't exist in an A-Math set
        if str(tile_desired) not in Tile.point_value_dict.keys():
            print("WARNING: The tile you've attempted to retrieve from this rack doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            return

        try:
            #using next should be consistently faster than using a map
            #note automatic attempt at conversion to str in case input was int.
            tile_drawn = next(tile for tile in self.tiles_on_rack \
                              if tile.pot == str(tile_desired))

        #if there are none of the desired tile left in the tilebag
        #give option of expanding tilebag with additional tile of interest.
        except StopIteration:
            print('You are attempting to draw a tile that is not present on this rack.')
            return
          
        #unless we've already cleared out because of an exception, remove the chosen tile from bag and return the Tile object removed.
        self.tiles_on_rack.remove(tile_drawn)
        return tile_drawn
        
                  
    ## function to print out tiles on rack nicely
    ## eventually, will allow user to change display order.
    def print_tiles_on_rack(self):
        sorted_rack = sorted(self.tiles_on_rack, key = lambda x: (x.tile_type, x))
        print(' '.join([ x.pot for x in sorted_rack ]))
        
    
    def exchange_tiles(self, tb):
        return 3