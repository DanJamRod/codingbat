def fix_teen(n):
    """ that takes in an int value and returns that value fixed for the teen rule
    """
    if 13<=n<=14 or 17<=n<=19:
        return 0
    else:
        return n

def no_teen_sum(a, b, c):
    """ Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens.
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
 
print(no_teen_sum(2, 13, 1))