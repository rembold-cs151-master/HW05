########################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
########################################


def Part_A(max_n):
    """
    """
    total = 0
    for i in range(max_n+1):
        if i % 3 == 0:
            total += i
    return total


def Part_B(phrase, des_letter):
    """
    """
    count = 0
    trim_str = ""
    for L in phrase:
        if L == des_letter:
            count += 1
        else:
            trim_str += L
    return count, trim_str


def Part_C(num):
    """
    """
    for i in range(1,num):
        if i**3 == num:
            return True
    return False
