## Fourth class built as part of Jesse Day's A-Math solver HAZMAT.
## An ongoing board object is saved as a 2D numpy array of Tile objects.

import numpy as np

from Rack import Rack
from Tile import Tile
from Tilebag import Tilebag

## standard convention used throughout program is that numbers denote rows, letters denote columns.
## a square on the board should be indicated with row first, e.g. 7A, 9J etc.

## Functions implemented:

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
    
    ##squares listed below in order TES, DES, TTS, DTS
    board_layout_dict = {'1A': 'TES', '15A': 'TES',  '1O': 'TES', '15O': 'TES', \
                         '1H': 'TES',  '8A': 'TES',  '8O': 'TES', '15H': 'TES', \
                         '2B': 'DES',  '3C': 'DES',  '4D': 'DES', \
                         '2N': 'DES',  '3M': 'DES',  '4L': 'DES', \
                        '14B': 'DES', '13C': 'DES', '12D': 'DES', \
                        '14N': 'DES', '13M': 'DES', '12L': 'DES', \
                         '5E': 'TTS',  '6F': 'TTS',  '6B': 'TTS',  '2F': 'TTS', \
                         '5K': 'TTS',  '6J': 'TTS',  '6N': 'TTS',  '2J': 'TTS', \
                        '11E': 'TTS', '10F': 'TTS', '10B': 'TTS', '14F': 'TTS', \
                        '11K': 'TTS', '10J': 'TTS', '10N': 'TTS', '14J': 'TTS', \
                         '8H': 'TTS', \
                         '1D': 'DTS',  '3G': 'DTS',  '4A': 'DTS',  '7C': 'DTS', '7G': 'DTS', \
                         '1L': 'DTS',  '3I': 'DTS',  '4O': 'DTS',  '7M': 'DTS', '7I': 'DTS', \
                        '15D': 'DTS', '13G': 'DTS', '12A': 'DTS',  '9C': 'DTS', '9G': 'DTS', \
                        '15L': 'DTS', '13I': 'DTS', '12O': 'DTS',  '9M': 'DTS', '9I': 'DTS', \
                         '4H': 'DTS',  '8D': 'DTS',  '8L': 'DTS', '12H': 'DTS'}
    
    ## initialize a board with layout listed above in board_layout_dict.
    def __init__(self):
        
        self.tiles_on_board = np.empty([15,15])
    
    # convention used throughout the program - numbers = rows, letters = columns, spaces described in row-column order (15C, 12D)
    def add_tile_to_board(self, Tile, pos):
        
        try:
            row = int(pos[:-1])
            col = pos[-1]
        except ValueError:    
            print('format wrong')
            return
                         
        if col.upper() not in [ chr(i) for i in range(ord('A'),ord('O')+1) ]:
            print("You did not input a legal placement for this tile.")
            print("Rows should be numbers in range 1-15, Columns should be letters in range A-O")
            print("Squares on the board should be referred to in row-column order (e.g. 3A, 14N).")
            return
        
        if 
        
        
        ## check if square already has a tile in it                                                                  
        
        
    def add_play_to_board(self):
        return 2
                         
    def score_play(self):
        return 3