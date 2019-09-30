##################################################
# Name:
# Collaborators:
# Est Time spent (hrs):
##################################################


def births(): #<-- fill in needed formal parameters
    """
    Function to compute the number of rabbits births each year.

    Assumes that rabbits have a single mate over the course of the year
    and can adjust gender as needed to produce offspring. Unpaired rabbits
    produce no offspring.

    Inputs:
        - N (int): the current number of rabbits breeding that year
        - brood (int): the number of baby rabbits that result from each mating pair

    Outputs:
        - (int) the number of baby rabbits born that year
    """
    pass #<-- comment or delete once you add your code


def rabbit_pop(): # <-- fill in needed formal parameters
    """
    Recursive function which computes the total rabbit population 
    after t years, assuming a birth rate given by births() and that 
    each rabbit lives 4 years before dying.

    Rabbit populations are assumed to start at 2 rabbits and brood
    sizes to be 4 new rabbits per pairing.

    Inputs:
        - t (int): desired year or generation

    Outputs:
        - (int): the number of rabbits alive after t years
    """
    pass #<-- comment or delete once you add your code


def rabbit_pop_w_wolves(): # <-- fill in needed formal parameters
    """
    Recursive function which computes the total rabbit population
    after t years, factoring in births, deaths, and wolf predators.

    Rabbit populations are assumed to start at 2 rabbits and brood
    sizes to be 4 new rabbits per pairing. Wolves consume rabbits
    with an alpha of 0.1.

    Inputs:
        - t (int): desired year or generation

    Outputs:
        - (int): the number of rabbits alive after t years
    """
    pass #<-- comment or delete once you add your code


def calc_needed_wolves(): # <-- fill in needed formal parameters
    """
    Function which computes the minimum needed amount of wolves to ensure
    the rabbit population is under 1000 after 10 years. Can use whatever numeric
    solving technique you prefer that applies to this situation. The desired
    accuracy is simply that you have less than 1000 rabbits alive after 10 years,
    and that you used the least amount of wolves to achieve that.

    Inputs:
        - None

    Outputs:
        - (int): the least number of wolves required
    """
    pass #<-- comment or delete once you add your code


# --------------
# All code should be contained in the above functions
# If you want to add code to automatically run your functions for
# testing purposes, make sure it is inside the below if statement

if __name__ == '__main__':
    pass
