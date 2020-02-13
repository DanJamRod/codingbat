def array123(nums):
    """ Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
    """
    count = 0
    for i in range (len(nums)):
        if nums[i:i+3] == [1, 2, 3]:
            count += 1
    return count > 0

# print(array123([1, 1, 2, 3, 1]))
# print(array123([1, 1, 1, 2, 3]))
# print(array123([1, 1, 2, 2, 1]))