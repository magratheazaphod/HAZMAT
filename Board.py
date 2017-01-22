## Fourth class built as part of Jesse Day's A-Math solver HAZMAT.

class Board:

    ## four types of tile possible on the board:
    ## DTS - Double Tile Score
    ## TTS - Triple Tile Score
    ## DES - Double Equation Score
    ## TES - Triple Equation Score
    
    ##below, the typical board layout of an A-Math set
    ##NOTE: Slightly different from layout of Scrabble board:
    # 1) Center start is a TTS, not a DWS;
    # 2) DWS tiles at E5, K5, E11 and K11 switched to TTS.
    
    board_layout_dict = {'0': 1, '1': 1,  '2': 1,  '3': 1, '4': 2,  '5': 2, \
                        '6': 2, '7': 2,  '8': 2,  '9': 2,'10': 3, '11': 4, \
                       '12': 3,'13': 6, '14': 4, '15': 4,'16': 4, '17': 6, \
                       '18': 4,'19': 7, '20': 5,  '+': 2, '-': 2,  '?': 0, \
                        '*': 2, '/': 2,'+|-': 1,'*|/': 1, '=': 1}
    
    def __init__(self, printed_on_tile):
        
        #if we just provide a number instead of number-as-string, converts to string
        if type(printed_on_tile) == int:
            self.pot = str(printed_on_tile)
        else:
            self.pot = printed_on_tile 
        
        #Assign point value (checks if actually a real tile!)
        try:
            self.point_value = self.point_value_dict[self.pot]
        except KeyError:
            print("WARNING: The tile you've attempted to create doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            print("Tile was NOT fully created.")
            
        self.tile_type = self.determine_type()
        
    def add_tile_to_board(self, Tile):
        return 1
        
    def add_play_to_board(self):
        return 2