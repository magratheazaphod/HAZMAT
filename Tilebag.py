#Tilebag class as part of HAZMAT - Jesse Day's A-Math solver.
#A collection of Tile objects and related operations (see class).
#Also attempted to implement as a dictionary showing quantities of each tile remaining, but this way makes random drawing easier.

#Functions: -FillBag (fill a brand new tile bag with Tile objects)
#           -HowManyInBag (check how many tiles there are total in bag, or check particular type of tile or particular denomination
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
               
                
    def HowManyInBag(self, Filter=""): #check how many tiles there are of a particular denomination in the bag
        
        if Filter.lower() in 'onedigit': #case insensitive
            mymap = map(lambda x: x.Type == 'OneDigit', self.TilesInBag)
        
        elif Filter.lower() == 'twodigit': #case insensitive
            mymap = map(lambda x: x.Type == 'TwoDigit', self.TilesInBag)
        
        elif Filter.lower() in ['number', 'numbers']: #can check for number OR numbers
            mymap = map(lambda x: (x.Type == 'OneDigit') | (x.Type == 'TwoDigit'), self.TilesInBag)
            
        elif Filter.lower() in ['operator', 'operators']: #more flexible query
            mymap = map(lambda x: x.Type == 'Operator', self.TilesInBag)
            
        elif Filter.lower() in ['blank', 'blanks']: #same as above, more flexible query
            mymap = map(lambda x: x.Type == 'Blank', self.TilesInBag)
        
        #if it's not a type filter, then checks for how many tiles match given denomination
        elif Filter: 
            if Filter in self.BaseTileDistribution.keys():
                mymap = map(lambda x: x.POT == Filter, self.TilesInBag)
            else:
                print('This is not a tile denomation or tile type included in a standard A-Math set.')
                print('Valid types to search for include OneDigit, TwoDigit, number, Operator and Blank.')
                return
            
        else: # if no filter is given, just counts how many tiles are in the bag
            mymap = map(lambda x: True, self.TilesInBag)
            
        num = sum(mymap)
        return num  
            
        
    def AddTileToBag(self, Denomination): #checks if we're somehow trying to add a tile beyond what's supposed to be in the bag
        
        try:
            
            print(self.BaseTileDistribution[Denomination])
            print(self.HowManyInBag(Denomination))
            
            if self.HowManyInBag(Denomination) >= self.BaseTileDistribution[Denomination]:
                print('WARNING: You are adding another', Denomination, 'even though this exceeds the standard distribution.')
                override = input('Are you sure you want to continue? (n)o or (y)es:')
            
                if override.lower() not in ['y', 'yes']:
                    print('Did not add tile in question.')
                    return
        
            self.TilesInBag.append(Tile.Tile(Denomination))
        
        except KeyError:
            print("WARNING: The tile you've attempted to add doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            print("Tile was NOT added to tilebag.")
            
                
    def DrawTile(self, TileDesired = 'rand'):

        #if thing in self: some_list.remove(thing)
            
        TileDrawn = rnd.choice(self.TilesInBag)
        self.Distribution[TileDrawn.POT] -= 1
        
    #def SwapTiles(self):        
    
    #def PrintBag:   #Print out contents of tilebag