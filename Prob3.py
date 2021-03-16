##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

autochecks = False # Set this to True if you want autochecks to run on this problem

mine_locations = [
        [ True  , False , False , False , False , True],
        [ False , False , False , False , False , True],
        [ True  , True  , False , True  , False , True],
        [ True  , False , False , False , False , False],
        [ False , False , True  , False , False , False],
        [ False , False , False , False , False , False]
    ]

# If you want to test more
alt_locations = [
        [ False , False , True  , False , False , False],
        [ True  , False , False , False , False , True],
        [ True  , False , False , False , False , False],
        [ False , False , False , True  , False , True],
        [ False , False , True  , False , False , False],
        [ True  , True  , False , True  , False , True],
    ]



def check_index_location(row, col, loc):
    """
    Function which checks to see how many bombs in `loc` are in
    the neighborhood of the given point, where 'neighborhood' is
    defined as locations within one space, above, below, left,
    right, or diagonal to the given point. If the given point
    is itself a bomb, a -1 should be returned instead.

    Args:
        row (int): Row index of the point to check
        col (int): Col index of the point to check
        loc (list of boolean lists): Boolean array with mine locations

    Returns
        (int): Either -1 if the given location is a bomb itself,
               or some value >=0 according to the number of neighbors
               that are bombs.
    """
    pass






def count_mines(loc):
    """
    Function to count the numbering neighboring mines at each point
    in the array and return an array of the counts at each space.

    Args:
        loc (list of boolean lists): Boolean array with mine locations

    Returns:
        (list of integer lists): List of lists of integers which
            indicate the number of neigboring bombs.
    """
    pass


if __name__ == '__main__':
    print(check_index_location(0,0,mine_locations))
    # Uncomment below once you have count_mines done
    # counts = count_mines(mine_locations)
    # for row in counts: # just for nicer printing
        # print(row)
