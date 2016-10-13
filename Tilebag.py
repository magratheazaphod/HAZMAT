#Tilebag class as part of HAZMAT - Jesse Day's A-Math solver.
#A collection of Tile objects and related operations (see class).
#Also attempted to implement as a dictionary showing quantities of each tile remaining, but this way makes random drawing easier.

#Functions: -Fill (a brand new tile bag)
#           -DrawTile (Returns tile object and updated tilebag with tile removed)
#           -Exchange (Replace inputted tiles with new random tiles

import Tile
import numpy.random as rnd

class Tilebag:
    
    BaseTileDistribution = {'0': 5, '1': 6,  '2': 6,  '3': 5, '4': 5,  '5': 4, \
                        '6': 4, '7': 4,  '8': 4,  '9': 4,'10': 2, '11': 1, \
                       '12': 2,'13': 1, '14': 1, '15': 1,'16': 1, '17': 1, \
                       '18': 1,'19': 1, '20': 1,  '+': 4, '-': 4,  '?': 4, \
                        '*': 4, '/': 4,'+|-': 5,'*|/': 4, '=': 11}
    
    def __init__(self): #creates a zero dictionary showing current tiles in tilebag, and also stores all current tiles as array
        
        #self.Distribution = dict.fromkeys(self.BaseTileDistribution, 0)
        self.TilesInBag = []
        
        
    def FillBag(self): #set bag to reference tile distribution
                
        #self.Distribution = self.BaseTileDistribution    
        
        for k, v in self.BaseTileDistribution.items():
            for i in range(v): #add multiple copies of each tile to tilebag depending on how many are supposed to be in there
                self.AddTileToBag(k) #handled in external function
        
        
    def AddTileToBag(self, Denomination): #checks if we're somehow trying to add a tile beyond what's supposed to be in the bag
        
        if self.BaseTileDistribution[Denomination] >= self.TilesInBag
        
        
        self.TilesInBag.append(Tile.Tile(k))
        yesno = input('Are you sure you want to continue? (y)es or (n)o:')
                
    def DrawTile(self, TileDesired = 'rand'):

        #if thing in self: some_list.remove(thing)
            
        TileDrawn = rnd.choice(self.TilesInBag)
        self.Distribution[TileDrawn.POT] -= 1
        
    #def SwapTiles(self):        