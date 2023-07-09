# Global variables to save values
compare = 0
move = 0

# Function to add 1 more in comparison
def comparisons():
    global compare
    compare = compare + 1

# Function to add 1 more in movement
def moves():
    global move
    move = move + 1

# Function to clear the values of global variables "move and compare"
def clear():
    global move, compare
    compare = 0
    move = 0

# Function that returns the result to main of the total movements and comparisons performed in the QuickSort algorithm
def results():
    global compare, move

    return compare, move