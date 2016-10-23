#Tilebag class as part of HAZMAT - Jesse Day's A-Math solver.
#A collection of Tile objects and related operations (see class).
#Also attempted to implement as a dictionary showing quantities of each tile remaining, but this way makes random drawing easier.

#Functions: -FillBag (fill a brand new tile bag with Tile objects)
#           -HowManyInBag (check how many tiles there are total in bag, or check particular type of tile or particular denomination
#           -DrawTile (Returns tile object and updated tilebag with tile removed)
#           -Exchange (Replace inputted tiles with new random tiles

from Tile import Tile
import numpy.random as rnd

class Tilebag:
    
    base_tile_distribution = {'0': 5, '1': 6,  '2': 6,  '3': 5, '4': 5,  '5': 4, \
                              '6': 4, '7': 4,  '8': 4,  '9': 4,'10': 2, '11': 1, \
                             '12': 2,'13': 1, '14': 1, '15': 1,'16': 1, '17': 1, \
                             '18': 1,'19': 1, '20': 1,  '+': 4, '-': 4,  '?': 4, \
                              '*': 4, '/': 4,'+|-': 5,'*|/': 4, '=': 11}
    
    def __init__(self): #creates a zero dictionary showing current tiles in tilebag, and also stores all current tiles as array
        
        self.tiles_in_bag = []
        
        
    def fill_bag(self): #set bag to reference tile distribution
                        
        for k, v in self.base_tile_distribution.items():
            for i in range(v): #add multiple copies of each tile to tilebag depending on how many are supposed to be in there
                self.add_tile_to_bag(k) #handled in external function
               
                
    def how_many_in_bag(self, myfilter=""): #check how many tiles there are of a particular denomination in the bag
        
        if type(myfilter) == int: #if user put in an integer, start by converting to a string
            Filter = str(Filter)
        
        if myfilter.lower() == 'onedigit': #case insensitive
            mymap = map(lambda x: x.Type == 'OneDigit', self.tiles_in_bag)
        
        elif myfilter.lower() == 'twodigit': #case insensitive
            mymap = map(lambda x: x.Type == 'TwoDigit', self.tiles_in_bag)
        
        elif myfilter.lower() in ['number', 'numbers']: #can check for number OR numbers
            mymap = map(lambda x: (x.Type == 'OneDigit') | (x.Type == 'TwoDigit'), self.tiles_in_bag)
            
        elif myfilter.lower() in ['operator', 'operators']: #more flexible query
            mymap = map(lambda x: x.Type == 'Operator', self.tiles_in_bag)
            
        elif myfilter.lower() in ['blank', 'blanks']: #same as above, more flexible query
            mymap = map(lambda x: x.Type == 'Blank', self.tiles_in_bag)
        
        #if it's not a type filter, then checks for how many tiles match given denomination
        elif myfilter: 
            if myfilter in self.base_tile_distribution.keys():
                mymap = map(lambda x: x.POT == myfilter, self.tiles_in_bag)
            else:
                print('This is not a tile denomation or tile type included in a standard A-Math set.')
                print('Valid types to search for include OneDigit, TwoDigit, number, Operator and Blank.')
                return
            
        else: # if no filter is given, just counts how many tiles are in the bag
            mymap = map(lambda x: True, self.tiles_in_bag)
            
        num = sum(mymap)
        return num  
            
        
    def add_tile_to_bag(self, denomination): #checks if we're somehow trying to add a tile beyond what's supposed to be in the bag
        
        try:
            #order matters on next line - checks for key error first before trying to see how many are in bag
            if self.base_tile_distribution[denomination] <= self.how_many_in_bag(denomination):
                print('WARNING: You are adding another', denomination, 'even though this exceeds the standard distribution.')
                override = input('Are you sure you want to continue? (n)o or (y)es:')
            
                if override.lower() not in ['y', 'yes']:
                    print('Did not add tile in question.')
                    return
        
            self.tiles_in_bag.append(Tile(denomination))
        
        except KeyError:
            print("WARNING: The tile you've attempted to add doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            print("Tile was NOT added to tilebag.")
            
            
    def print_bag(self):   #Print out contents of tilebag           
    
        sorted_bag = self.base_tile_distribution.keys()
    
        for denomination in sorted(self.base_tile_distribution, key = lambda x: (Tile.return_type(denomination), x)):
            nn = self.how_many_in_bag(denomination)
            print((nn-1) * (denomination + ",") + denomination)
            
                
    #def DrawTile(self, TileDesired = 'rand'):

        #if thing in self: some_list.remove(thing)
            
        #TileDrawn = rnd.choice(self.TilesInBag)
        #self.Distribution[TileDrawn.POT] -= 1
        
    #def SwapTiles(self):        
    
