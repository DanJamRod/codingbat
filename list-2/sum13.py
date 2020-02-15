def sum13(nums):
    """ Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i == len(nums)-1:
                break
            else:
                nums[i+1] = 0
        count += nums[i]
    return count

print(sum13([1, 2, 2, 1, 13, 1, 1]))