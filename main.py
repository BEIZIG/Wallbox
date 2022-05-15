import pytest

def get_minimum_index_value(index1,index2,vector1,vector2):
    result = vector1[index1]
    if index2 < index1 :
        return vector2[index2]
    return result

def find_first_duplicate(vector):
    result = None
    for i in vector:
        if vector.count(i) > 1 :
            return vector.index(i)
    return result
def find_first_in_vector(vector1,vector2):
    result =  None
    for i in vector1 :
        if i in vector2:
            return vector1.index(i)
    return result

def first_repeated_between_two_vector(vector1, vector2):
    result = None
    index1 = find_first_duplicate(vector1)
    index2 = find_first_duplicate(vector2)
    if index1 != None and index2 != None :
        return get_minimum_index_value(index1, index2, vector1, vector2)
    return result

#Positive test cases
def test_method_1():
    assert first_repeated_between_two_vector([17,8,12],[2,16,6]) == None
#Negative test cases
def test_method_2():
    assert first_repeated_between_two_vector([16,16,12],[8,16,17,17]) == 16