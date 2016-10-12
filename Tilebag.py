#Tilebag class as part of HAZMAT - Jesse Day's A-Math solver.
#A collection of Tile objects and related operations (see class).

#Functions: -Fill (a brand new tile bag)
#           -DrawTile (Returns tile object and updated tilebag with tile removed)
#           -Exchange (Replace inputted tiles with new random tiles

import Tile

class Tilebag:
    
    TileDistribution = {'0': 5, '1': 6,  '2': 6,  '3': 5, '4': 5,  '5': 4, \
                        '6': 4, '7': 4,  '8': 4,  '9': 4,'10': 2, '11': 1, \
                       '12': 2,'13': 1, '14': 1, '15': 1,'16': 1, '17': 1, \
                       '18': 1,'19': 1, '20': 1,  '+': 4, '-': 4,  '?': 4, \
                        '*': 4, '/': 4,'+|-': 5,'*|/': 4, '=': 11}
    
    def __init__(self): #creates empty tilebag object
        self.InBag = []

    def FillBag(self):
        
        for k, v in self.TileDistribution.items():
            for i in range(v):
                
                self.InBag.append(Tile.Tile(k))
                
    #def DrawTile(self):
        
    #def SwapTiles(self):
