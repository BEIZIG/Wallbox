# A function that given 2 vectors of integers finds the first repeated number
# ****************************methods to be tested****************************


def check_vector_type(vector, input_type):
    for i in vector:
        if not isinstance(i, input_type):
            return False
    return True

def get_minimum_index_value(index1, index2, vector1, vector2):
    result = vector1[index1]
    if index2 < index1:
        return vector2[index2]
    return result


def find_first_duplicated_in_two_vectors(vector1, vector2):
    result = None
    for i in vector1:
        if i in vector2:
            return vector1.index(i)
    return result


def first_repeated_element(vector1, vector2):
    result = None
    check1 = check_vector_type(vector1, int)
    check2 = check_vector_type(vector2, int)
    if (not check1) or (not check2):
        return 'please enter two vectors of integer'
    index1 = find_first_duplicated_in_two_vectors(vector1, vector2)
    index2 = find_first_duplicated_in_two_vectors(vector2, vector1)
    if (index1!=None) and (index2!=None):
        return get_minimum_index_value(index1, index2, vector1, vector2)
    return result



