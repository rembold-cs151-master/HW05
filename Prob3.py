##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################


def is_flush(): # <-- provided any needed formal parameters
    """
    Function which takes a string of standard cards and returns
    whether or not a flush is present (if all 5 cards have the same
    suit).

    Inputs:
        - cards (str): String of the 5 card hand with 2 character
                       descriptions of card value at suit

    Outputs:
        - (bool): Whether or not the hand contains a flush
    """
    pass # <-- remove or comment out once you add your code



def count_flushes(): # <-- provide any needed formal parameters
    """
    Function which reads in a large batch of poker hands from hands.txt.
    Each line contains two hands, with individual cards separated by a
    space. The number of flushes is counted and returned by the function.

    In addition, the function writes each hand containing a flush to the
    file flushes.txt, where each new line will contain one hand that
    contained a flush. You might be appending to that file here, but
    make sure that if you run the program multiple times you only get
    the latest runs lines added to the file!

    Inputs:
        - filename (str): filename of file with sets of poker hands

    Outputs:
        - (int) The number of hands found that were flushes
    """
    pass # <-- remove or comment out once you add your code


if __name__ == '__main__':
    print(count_flushes('hands.txt'))
