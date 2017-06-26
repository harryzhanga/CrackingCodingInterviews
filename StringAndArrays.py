#1.1
def has_unique_char(string):
    #uses dictionary (more data)
    char_dict= {}
    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = 1
    return True

def has_unique_char_2(string):
    #without extra data
    string = sorted(list(string))
    #check if any character is the same as the previous
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return False
    return True

#1.2
def reverse_C_string(string):
    return string[-1::-1] + "\0"

def reverse_C_string_2(string):
    new_str = ""
    i = len(string) - 2
    while i >= 0:
        new_str += string[i]
        i -= 1
    new_str += "\0"
    return new_str
