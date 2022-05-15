import random
import pytest
from functions import first_repeated_element
# ************************methods to generate test data************************
def generate_two_non_intersecting_vectors(x):
    # Generate 2*X random numbers between 0 and 200
    randomvector = list(set(random.sample(range(0, 200), 2 * x)))
    return randomvector[0:x], randomvector[x + 1:]


def positionate_intersecting_vectors(x,i,j):
    # Generate 2*X random numbers between 0 and 200
    randomvector = list(set(random.sample(range(0, 200), 2*x)))
    vector1 = randomvector[0:x]
    vector2 = randomvector[x:]
    value1 = random.randint(0, 100)
    vector1[i] = value1
    vector2[j] = value1
    return vector1, vector2

# ********************************test cases********************************
# data driven test
x = random.randint(10, 100)
#in this case we have two integer vectors with two duplicated elements
# i : index of anticipated duplicated position inside vector1
# j : index of anticipated duplicated position inside vector2
# in this case i < j --> we expect to find vector1[i] as first repeated number
i = x-5
j = x-2
vector1, vector2 = positionate_intersecting_vectors(x, i, j)
inputData1 = (vector1, vector2, vector1[i])

# in this case j < i --> we expect to find vector2[j] as first repeated number
i = x-5
j = x-9
vector1, vector2 = positionate_intersecting_vectors(x, i, j)
inputData2 = (vector1, vector2, vector2[j])

#Negative test cases
vector1, vector2 = generate_two_non_intersecting_vectors(x)
inputData3 = (vector1, vector2, None)

x = random.randint(0, 100)
vector1 = list(set(random.sample(range(0, 200), x)))
vector2 = []
inputData4 = (vector1, vector2, None)

inputData = [inputData1, inputData2, inputData3, inputData4]

@pytest.mark.parametrize("vector1,vector2,result",inputData)
def test_method_1(vector1, vector2, result):
    assert first_repeated_element(vector1, vector2) == result

#one of the vector has a float element
input1 = ([1.2, 5, 4], [], 'please enter two vectors of integer')
#one of the vector has a String element
input2 = ([], ['foo', 5, 4], 'please enter two vectors of integer')
input = [input1, input2]


@pytest.mark.parametrize("vect1,vect2,res", input)
def test_method_2(vect1, vect2, res):
    assert first_repeated_element(vect1, vect2) == res
