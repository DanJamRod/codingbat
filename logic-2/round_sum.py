def round_sum(a, b, c):
    """ For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values.
    """
    return int(round(a,-1) + round(b,-1) + round(c,-1))

print(round_sum(12, 15, 18))    