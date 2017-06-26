#1.1
def has_unique_char(string):
    #uses dictionary (more data) but O(n)
    char_dict= {}
    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = 1
    return True

def has_unique_char_2(string):
    #without extra data but O(nlogn) run time
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


#1.4
def are_anagrams(str1, str2):
    #using sorting O(logn)
    return sorted(str1) == sorted(str2)

def are_anagrams_2(str1, str2):
    #O(n) memory but decreases run time to O(n)
    str1_counts = {}
    for char in str1:
        str1_counts[char] = str1_counts.get(char, 0) + 1
    
    str2_counts = {}
    for char in str2:
        str2_counts[char] = str2_counts.get(char, 0) + 1
    
    for char in str1 + str2:
        if char not in str1_counts or char not in str2_counts or str1_counts[char] != str2_counts[char]:
            return False
    return True
