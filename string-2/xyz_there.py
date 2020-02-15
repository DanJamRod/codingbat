def xyz_there(str):
    """ Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    """
    flag = False
    for i in range (len(str)-2):
        if str[i:i+3] == "xyz" and str[i-1]!=".":
            flag = True
    return flag

print(xyz_there('abcxyz'))
# print(xyz_there('abc.xyzxyzabc'))
# print(xyz_there('ab'))