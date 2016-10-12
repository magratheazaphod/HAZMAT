#Tile class used as part of HAZMAT, Jesse's first try at an A-Math solver.
#Initializes tiles correctly
class Tile:

    PointValueDict = {'0': 1, '1': 1,  '2': 1,  '3': 1, '4': 2,  '5': 2, \
                      '6': 2, '7': 2,  '8': 2,  '9': 2,'10': 3, '11': 4, \
                     '12': 3,'13': 6, '14': 4, '15': 4,'16': 4, '17': 6, \
                     '18': 4,'19': 7, '20': 5,  '+': 2, '-': 2,  '?': 0, \
                      '*': 2, '/': 2,'+|-': 1,'*|/': 1, '=': 1}
    #This is a dictionary that associated what's on the tile with a fixed point value and a type.
    #"Type" can be one of three: Operator, one-digit number and two-digit number.
    #Reason for distinguishing one- and two-digit numbers is because you're allowed to
    #chain one-digit numbers on the board (up to 3 in a row total), but NO chaining 
    #allowed with two-digit numbers.
    
    def __init__(self, PrintedOnTile):
        self.POT = PrintedOnTile 
        
        #Assign point value (checks if actually a real tile!)
        try:
            self.PointValue = self.PointValueDict[PrintedOnTile]
        except KeyError:
            print("WARNING: The tile you've attempted to create doesn't exist in A-Math!")
            print("Tiles should have a value between 0 or 20, be an operator (+, -, *, /, +|-, *|/ or =) or a blank (?).")
            print("Tile was NOT created.")
            
        self.Type = self.DetermineType()

    def DetermineType(self):
        if self.POT == '?':
            return 'Blank'
        
        #Check if integer, and if so, check if one or two digits - two digit numbers cannot be concatenated with other numbers.
        elif str.isdigit(self.POT):
            if len(self.POT) == 1:
                return 'OneDigit'
            else:
                return 'TwoDigit'
                
        else: #exhausted all other options. Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth. Er, type.
            return 'Operator'
