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

#1.5
def replace_with(prev, new, string):
    #using just the pure python string library. Expected O(n)
    return string.replace(prev, new)

def replace_with_2(prev, new, string):
    #for now, I will expect that prev is just one character and not many characters
    #this is O(n)
    new_str = ""
    for char in string:
        if char == prev:
            new_str += new
        else:
            new_str += char
    return new_str


#1.6
def rotate_image(image):
    #image is given as list of lists
    #this is rotation in place by 90 degrees clockwise
    return zip(*image[::-1])

def rotate_image_2(image):
    #if rotation by 90 degrees anti clockwise
    return zip(*image)[::-1]

#the long way using helper functions
def swap(a, y, x):
    pos1 = (y, x)
    pos2 = (x, len(a)-1-y)
    temp = a[pos1[0]][pos1[1]]
    a[pos1[0]][pos1[1]] = a[pos2[0]][pos2[1]]
    a[pos2[0]][pos2[1]] = temp

def rotate_layer(a, layer):
    max_index = len(a)-1
    for i in range(layer, max_index-layer+1):
        swap(a, max_index-layer, i)
    
    for j in range(layer, max_index-layer):
        swap(a, j, max_index-layer)
    
    for i in range(layer+1, max_index-layer):
        swap(a, layer, i)

def rotateImage(a):
    #rotate image in place by 90 degrees clockwise
    for i in range(0, int(len(a)/2)):
        rotate_layer(a, i)
    return a

#1.7
def replace(row, prev, sentinel):
    for index, elem in enumerate(row):
        if elem != prev:
            row[index] = sentinel
    return row

def replace_with(prev, new, matrix, sentinel):
    #done in place for an MxN matrix. This is O(m*n). 
    #This requires O(1) space. While the textbook solution requires O(m+n) space 
    matrix = [replace(row, prev, sentinel) if prev in row else row for row in matrix]
    matrix = [list(row) for row in zip(*matrix)]
    matrix = [replace(row, prev, sentinel) if prev in row else row for row in matrix]
    matrix = [list(row) for row in zip(*matrix)]
    for row in matrix:
        for index, elem in enumerate(row):
            if elem == sentinel:
                row[index] = new
    return matrix

#an example of how this funtion could be used
matrix = [[0, 0, 1], [1, 1, 1], [1, 1, 2]]
replace_with(0, 0, matrix, "a")
