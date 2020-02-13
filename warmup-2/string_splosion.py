def string_splosion(str):
    """ Given a non-empty string like "Code" return a string like "CCoCodCode".
    """
    string_sploded = ""
    for i in range(len(str)+1):
        string_sploded = string_sploded + str[:i]
    return string_sploded
        
# print(string_splosion("Code"))