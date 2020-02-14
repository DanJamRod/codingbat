def sum3(nums):
    """ Given an array of ints length 3, return the sum of all the elements.
    """
    sum = 0
    for i in range (len(nums)):
        sum += nums[i]
    return sum

print(sum3([5, 11, 2]))