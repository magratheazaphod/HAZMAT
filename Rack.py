## Third module implemented for the HAZMAT A-math solver - manages rack dynamics.
## Each game of A-Math will contain two rack objects (although, no reason not to allow more for multiplayer games).

class Rack:
    
    def __init__(self):
        
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
