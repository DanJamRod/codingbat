def end_other(a, b):
    """ Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
    """
    c = max(a, b ,key=len)
    d = min(b, a ,key=len)
    return c[-len(d):].lower() == d.lower()

print(end_other('AbC', 'HiaBc'))
# print(end_other('abcXYZ', 'abcDEF'))