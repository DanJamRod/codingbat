def sum67(nums):
    """ Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i]==6:
            nums[i]=0
            if nums[i+1]==7:
                nums[i+1]=0
            else:
                nums[i+1]=6
        else:
            count += nums[i]
    return count

print(sum67([1, 2, 2, 6, 99, 99, 7]))