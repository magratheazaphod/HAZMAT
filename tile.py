#Tile class used as part of HAZMAT, Jesse's first try at an A-Math solver.
class Tile:

    PointValueDict = {'0': 1, '1': 1,  '2': 1,  '3': 1, '4': 2,  '5': 2, \
                      '6': 2, '7': 2,  '8': 2,  '9': 2,'10': 3, '11': 4, \
                     '12': 3,'13': 6, '14': 4, '15': 4,'16': 4, '17': 6, \
                     '18': 4,'19': 7, '20': 5,  '+': 2, '-': 2,  '?': 0, \
                      '*': 2, '/': 2,'+|-': 1,'*|/': 1}
    #This is a dictionary that associated what's on the tile with a fixed point value and a type.
    #"Type" can be one of three: Operator, one-digit number and two-digit number.
    #Reason for distinguishing one- and two-digit numbers is because you're allowed to
    #chain one-digit numbers on the board (up to 3 in a row total), but NO chaining 
    #allowed with two-digit numbers.
    
    def __init__(self, PrintedOnTile):
        self.POT = PrintedOnTile 
        self.PointValue = self.PointValueDict[PrintedOnTile]
        self.Type = 'Q'

#    def DetermineType(
