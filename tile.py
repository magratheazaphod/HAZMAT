#Tile class used as part of HAZMAT, Jesse's first try at an A-Math solver.
#Initializes tiles correctly
class Tile:

    point_value_dict = {'0': 1, '1': 1,  '2': 1,  '3': 1, '4': 2,  '5': 2, \
                        '6': 2, '7': 2,  '8': 2,  '9': 2,'10': 3, '11': 4, \
                       '12': 3,'13': 6, '14': 4, '15': 4,'16': 4, '17': 6, \
                       '18': 4,'19': 7, '20': 5,  '+': 2, '-': 2,  '?': 0, \
                        '*': 2, '/': 2,'+|-': 1,'*|/': 1, '=': 1}
    #dictionary with point value of each tile in the game, called when any Tile initialized.
    
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

    #instance method that gives tile type based on what is printed on tile.
    def determine_type(self):
        if self.pot == '?':
            return 'Blank'
        
        #Check if integer, and if so, check if one or two digits - two digit numbers cannot be concatenated with other numbers.
        elif str.isdigit(self.pot):
            if len(self.pot) == 1:
                return 'OneDigit'
            else:
                return 'TwoDigit'
                
        else: #exhausted all other options. Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth. Er, type.
            return 'Operator'
    
    #static method that gives type of tile given a denomination (equivalent to Tile.POT above)
    @staticmethod    
    def return_type(denomination):
        if denomination == '?':
            return 'Blank'

        #Check if integer, and if so, check if one or two digits - two digit numbers cannot be concatenated with other numbers.
        elif str.isdigit(denomination):
            if len(denomination) == 1:
                return 'OneDigit'
            elif int(denomination) < 21: #only gives TwoDigit for numbers 10-20.
                return 'TwoDigit'
            else:
                print('Your number is not included in the A-Math tile distribution (number tiles span from 0-20).')

        elif denomination in ('+','-','*','/','+|-','*|/','='):
            return 'Operator'
        
        else:
            print('Cannot determine type. Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).')
            return None