def has23(nums):
    """ Given an int array length 2, return True if it contains a 2 or a 3.
    """
    flag = False
    for i in range(len(nums)):
        if nums[i] == 2 or nums[i] == 3:
            flag += 1
    return bool(flag)

print(has23([2, 5]))
print(has23([4, 5]))
print(has23([2, 3]))