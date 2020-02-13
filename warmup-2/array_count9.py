def array_count9(nums):
    """ Given an array of ints, return the number of 9's in the array.
    """
    count = 0
    for nums in nums:
        if nums == 9:
            count += 1
    return count

# print(array_count9([1, 9, 9, 3, 9]))