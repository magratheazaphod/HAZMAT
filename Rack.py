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
## 1) The tiles that you want might be on the other players rack - have to be able to check for that case. May need a function like 'print_unseen'
## 2) Need to error test remove_tile and set_rack_to_input functions.

from Tile import Tile
from Tilebag import Tilebag

class Rack:
    
    tile_limit = 8 #could change to 7 to make more similar to Scrabble!
    exchange_cutoff = 5 #what is the minimum for unseen tiles for an exchange to be conducted?
    
    def __init__(self):
        self.tiles_on_rack = []  #will be filled with Tile objects by a Game calling function fill_rack.
        
        
    ## default: Fill rack back up to 8 tiles from Tilebag object tb
    ## is this the right way of doing this? currently not returning tilebag object, but editing in place.
    def fill_rack(self, tb):
        draw_how_many_tiles = min(Rack.tile_limit - len(self.tiles_on_rack), tb.how_many_in_bag())
        [ self.tiles_on_rack.append(tb.draw_tile()) for i in range(draw_how_many_tiles) ]
        
        
    ## set rack to input letters, with desired letters delimited by commas.
    def set_rack_to_input(self, target_rack, tb):
        
        # accept either spaces or commas to separate input.
        parsed_rack = [ x.strip() for x in target_rack.replace(',',' ').split(' ') ]
        
        if len(parsed_rack) > 8:
            override = input('Requested rack with over 8 tiles - are you sure? (n)o or (y)es:')
                  
            if override.lower() not in ['y', 'yes']:
                print('Did not adjust rack.')
                return
            
        tiles_back_to_bag = self.remove_tiles_from_rack() ## step 1 - remove tiles from rack
        [ tb.add_tile_to_bag(old_tile) for old_tile in tiles_back_to_bag ]  ## step 2 - return to tilebag
        new_tiles = [ tb.draw_tile(new_tile) for new_tile in parsed_rack ] ## step 3 - draw new tiles
        self.tiles_on_rack = [x for x in new_tiles if x is not None] ## step 4 - expunge Nones from unsuccessful drawing.
      
        
    # very similar to draw_tile module, except that we require a definite input of what tiles are being removed (no random option)
    # relies on calling function remove_single_tile for all tiles of interest
    # DEFAULT: if input isn't specified, clear rack of ALL tiles.
    def remove_tiles_from_rack(self, target_tiles = 'all'):
        
        removed_tiles = []
        
        ## default case - empty the rack and throw all tiles back into tilebag
        if target_tiles == 'all':
            parsed_tiles = [ x.pot for x in self.tiles_on_rack ]
        
        else: ## allow for removal of specific tiles - comma- or space-delimited
            parsed_tiles = [ x.strip() for x in target_tiles.replace(',',' ').split(' ') ]
            
        for next_tile in parsed_tiles:
            removed_tiles.append(self.remove_single_tile(next_tile))

        ## in case we unsuccessfully attempted to remove tiles, strip any Nones
        removed_tiles = [x for x in removed_tiles if x is not None]    
        return removed_tiles
    
    
    ##called above my remove_tiles_from_rack, removes a single tile from rack object.
    ##spits out the tile that was just removed from the rack.
    ##IMPORTANT: Input is not a Tile object, but the DENOMINATION of tile that we're looking for
    def remove_single_tile(self, target_tile):
                
        #if we try to draw a tile that doesn't exist in an A-Math set
        if str(target_tile) not in Tile.point_value_dict.keys():
            print("WARNING: The tile you've attempted to retrieve from this rack doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            return

        try:
            #using next should be consistently faster than using a map
            #note automatic attempt at conversion to str in case input was int.
            tile_chosen = next(tile for tile in self.tiles_on_rack \
                              if tile.pot == str(target_tile))

        #if there are none of the desired tile left in the tilebag
        #give option of expanding tilebag with additional tile of interest.
        except StopIteration:
            print('You are attempting to draw a tile that is not present on this rack.')
            return
          
        #unless we've already cleared out because of an exception, remove the chosen tile from bag and return the Tile object removed.
        self.tiles_on_rack.remove(tile_chosen)
        return tile_chosen        
                  
        
    ## function to print out tiles on rack nicely
    ## eventually, will allow user to change display order.
    def print_rack(self):
        sorted_rack = sorted(self.tiles_on_rack, key = lambda x: (x.tile_type, x.pot))
        print(' '.join([ x.pot for x in sorted_rack ]))
        
    
    ## relies on the versatile Tilebag.swap_tiles function
    ## According to printed rules, exchanges can only happen with 5 or more tiles in bag.
    def exchange_tiles(self, tb, tiles_to_exchange):

        parsed_exchange = [ x.strip() for x in tiles_to_exchange.replace(',',' ').split(' ') ]
        
        ## two cases in which exchange aborted - less than 5 in bag, or attempted to exchange
        ## too many tiles.
        if tb.how_many_in_bag() < 12:
            print('Cannot exchange with 5 tiles or fewer in bag!')
            return
        
        ##perform a quick check to make sure that the tiles to be exchanged are actually on rack
        currently_on_rack = [ tile.pot for tile in self.tiles_on_rack ]
        try:
            [ currently_on_rack.remove(x) for x in parsed_exchange ]
            
        except ValueError:
            print('You\'re attempting to exchange tiles that aren\'t currently on your rack.')
            override = input('Continue by exchanging as many tiles as possible from requested? (n)o or (y)es')
            if override not in ['y','yes']:
                print('Exchange aborted.')
                return
            
        print(42)
        
        ##since A-math allows exchanges with less than 8 in bag, check that we're not trying to exchange too many.
        if len(parsed_exchange) > tb.how_many_in_bag()-8:
            print('Not enough tiles in bag to exchange that many tiles.')
            print('Max possible exchange is',tb.how_many_in_bag()-8,'tiles')
            return
            
        tiles_back_to_bag = self.remove_tiles_from_rack(parsed_exchange) ## step 1 - remove tiles from rack
        [ tb.add_tile_to_bag(old_tile) for old_tile in tiles_back_to_bag ]  ## step 2 - return Tiles to tilebag
        new_tiles = [ tb.draw_tile() for new_tile in tiles_back_to_bag ] ## step 3 - draw equal number of replacement tiles
        self.tiles_on_rack = [x for x in new_tiles if x is not None] ## step 4 - expunge any Nones from unsuccessful drawing.