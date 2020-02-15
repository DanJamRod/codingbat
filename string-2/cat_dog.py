def count(str, substring):
    """ Counts number of times a substring is used in a string
    """
    count = 0
    for i in range (1+len(str)-len(substring)):
        if str[i:i+(len(substring))] == substring:
            count +=1
    return count

def cat_dog(str):
    """ Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return count(str, "cat") == count(str, "dog")

print(cat_dog("1cat1cadodog"))
# print(cat_dog("catdogcat"))