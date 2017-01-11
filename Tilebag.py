#Tilebag class as part of HAZMAT - Jesse Day's A-Math solver.
#A collection of Tile objects and related operations (see class).
#Also attempted to implement as a dictionary showing quantities of each tile remaining, but this way makes random drawing easier.

#Functions: -fill_bag (fill a brand new tile bag with Tile objects)
#           -how_many_in_bag (check how many tiles there are total in bag, or check particular type of tile or particular denomination
#           -add_tile_to_bag (adds a tile with specific domination to tilebag object)
#           -print_bag (prints all of the tiles currently contained in a tilebag object)
#           -draw_tile (Returns tile object and updated tilebag with tile removed)
#           -exchange_tile (Replace inputted tiles with new random tiles


### OUTSTANDING ISSUES
# 1) Get tilebag to print in a more sensible order (in fact, could even make this order customizable)
# 2) Should allow for interchangeability between *|/ and */, and also +|- and +- (the Chew convention)


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
                mymap = map(lambda x: x.pot == myfilter, self.tiles_in_bag)
            else:
                print('This is not a tile denomation or tile type included in a standard A-Math set.')
                print('Valid types to search for include OneDigit, TwoDigit, number, Operator and Blank.')
                return
            
        else: # if no filter is given, just counts how many tiles are in the bag
            mymap = map(lambda x: True, self.tiles_in_bag)
            
        num = sum(mymap)
        return num  
            
    #checks if we're somehow trying to add a tile beyond what's supposed to be in the bag    
    def add_tile_to_bag(self, denomination): 
        
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
            
    #Print out contents of tilebag  
    def print_bag(self):            
    
        sorted_bag = sorted(self.base_tile_distribution, key = lambda x: (Tile.return_type(x), x))
    
        for denomination in sorted_bag:
            nn = self.how_many_in_bag(denomination)
            
            if nn > 0: #shouldn't print line at all if none of that tile remaining in bag
                print((nn-1) * (denomination + ",") + denomination)
            
    #returns a tile object that will get added to a Rack object, and also updates Tilebag to remove chosen tile.    
    def draw_tile(self, tile_desired = 'rand'):

        #if thing in self: some_list.remove(thing)
        if tile_desired != 'rand':
            
            if str(tile_desired) not in Tile.point_value_dict.keys():
                print("WARNING: The tile you've attempted to draw doesn't exist in A-Math!")
                print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
                return
            
            else:
            
                try:
                    #using next should be consistently faster than using a map
                    #note automatic attempt at conversion to str in case input was int.
                    tile_drawn = next(tile for tile in self.tiles_in_bag \
                                      if tile.pot == str(tile_desired))

                #if we try to draw a tile that doesn't exist in an A-Math set


                #if there are none of the desired tile left in the tilebag
                except StopIteration:
                    print('There are no more of the desired tile in this tilebag. No tile drawn.')
                    return
            
        else:    
            #choose random tile object, then remove this object from tilebag.
            tile_drawn = rnd.choice(self.tiles_in_bag)
        
        #unless we've already cleared out because of an exception, remove the chosen tile from bag
        self.tiles_in_bag.remove(tile_drawn)        
        return tile_drawn
        
    #def exchange_tiles(self):        
    
