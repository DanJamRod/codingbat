def array_count9(nums):
    """ Given an array of ints, return the number of 9's in the array.
    """
    count = 0
    if len(nums) >= 4:
        for i in range (4):
            if nums[i] == 9:
                count += 1
        return count > 0
    else:
        for i in range (len(nums)):
            if nums[i] == 9:
                count += 1
        return count > 0

    # #Better solution:
    # end = len(nums)
    # if end > 4:
    #     end = 4
    # for i in range(end):
    #     if nums[i] == 9:
    #         return True
    # return False
 

# print(array_count9([1, 9, 9, 3, 9]))
# print(array_count9([0, 1, 2]))