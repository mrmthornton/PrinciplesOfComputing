"""
Clone of 2048 game.
"""

######import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    for index in range(len(line)): #combine "adjacent" cells in the line
        if line[index] == 0:
            continue
        for next in range(index+1,len(line)):
            if line[next] == 0:
                continue
            if line[index] == line[next]:
                line[index] = line[index] + line[next]
                line[next] = 0
                break
    for index in range(len(line)): #shift non-empty cells to the beginning of the line
        if line[index] != 0:
            continue
        for next in range(index+1,len(line)):
            if line[next] == 0:
                continue
            line[index] = line[next]
            line[next] = 0
            break                                  
    return [line]

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
        
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        #self.cells = [[ 0 for dummy_col in range(self.grid_width)]
        #              for dummy_row in range(self.grid_height)]
        pass
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.cells = [[ 0 for dummy_col in range(self.grid_width)]
                      for dummy_row in range(self.grid_height)]
        pass
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in range(self.grid_height):
            s = ""
            for col in range(self.grid_width):
                s += str(self.cells[row][col]) 
            print s     
        pass

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.cells[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.cells[row][col]
 
    
######poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
line = [2,0,2,2,2,0,4,0,2,4]
merge(line)
print line
merge(line)
print line
merge(line)
print line

test = TwentyFortyEight(4,5)
test.set_tile(1,1,1)
test.set_tile(2,2,2)
test.set_tile(3,3,3)
test.set_tile(3,4,8)
print test.get_tile(2, 3)
print test.get_grid_height()
print test.get_grid_width()
test.__str__()