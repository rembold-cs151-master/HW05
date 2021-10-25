##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################


def get_puzzles(filename):
    """
    Function to read in all the puzzles in the given filename. 
    This function is provided for your convenience and you don't
    need to do ANYTHING inside it!

    Args:
        filename (str): filename of the file containing the puzzles

    Returns:
        (list of puzzles): list of all available puzzles
                           Each puzzle is a list of lists of ints

    Usage:
    >>> puzzles = get_puzzles('puzzles.txt')
    >>> print(puzzles[0]) # for the first puzzle
    >>> print(puzzles[1]) # for the second puzzle, etc
    """
    puzzles = []
    single_puzzle = []
    with open(filename) as fh:
        for line in fh:
            if line == "\n":
                puzzles.append(single_puzzle)
                single_puzzle = []
            else:
                single_puzzle.append([int(i) for i in line.strip()])
    return puzzles



def is_valid_puzzle(): # <-- provide any needed formal parameters
    """
    Predicate function to take a single sudoku puzzle and determine
    if it is a valid puzzle. Valid puzzles should meet 3 criteria:
        - A single instance of each number 1-9 in each row
        - A single instance of each number 1-9 in each column
        - A single instance of each number 1-9 in each 3x3 section

    Args:
        puzzle (list of lists of ints): a single sudoku puzzle

    Returns:
        (bool): True if the puzzle is valid, False otherwise.
    """
    pass # <-- remove or comment out once you add your code


if __name__ == '__main__':
    puzzles = get_puzzles("puzzles.txt")
    puzzle_index = 0
    print(f"Puzzle Index {puzzle_index} is valid? {is_valid_puzzle(puzzles[puzzle_index])}")
