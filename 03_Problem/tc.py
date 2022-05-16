import random
import pytest
from functions import minimum_quantity_of_changes
# ************************methods to generate test data************************
def generate_interspersed_sequence(x,start):
    sequence = []
    sequence.append(start)
    for i in range(x):
        sequence.append(1-sequence[i])
    return sequence

def insert_n_modification(x, n, start):
    already_used = []
    sequence = generate_interspersed_sequence(x, start)
    for i in range(n):
        p = random.randint(0, x)
        while p in already_used:
            p = random.randint(0, x)
        sequence[p] = (1-sequence[p])
        already_used.append(p)
    return sequence
# ********************************test cases********************************


''' data driven test'''
x = random.randint(5, 100)
start = random.randint(0, 1)
expected_leading0 = generate_interspersed_sequence(x, 0)
expected_leading1 = generate_interspersed_sequence(x, 1)
'''in this case we have a sequence of one element we expect to have 0 as result'''
sequence1 = [random.randint(0, 1)]
inputData1 = (sequence1, 0, sequence1, sequence1)
'''in this case we have interspersed_sequence we expect to have 0 as result'''
sequence2 = generate_interspersed_sequence(x, start)
inputData2 = (sequence2, 0, expected_leading0, expected_leading1)
'''in this case we have non interspersed_sequence with modification < x/2 we expect to have p as result'''
p = random.randint(1, int(x/2)-1)
sequence3 = insert_n_modification(x, p, start)
inputData3 = (sequence3, p, expected_leading0, expected_leading1)


'''in this case we have non interspersed_sequence with modification > x/2 we expect to have x-p-+1 as result'''
p = random.randint(int(x/2)+1, x)
sequence4 = insert_n_modification(x, p, start)
inputData4 = (sequence4, x-p+1, expected_leading0, expected_leading1)
inputData_method1 = [inputData1,inputData2, inputData3, inputData4]


@pytest.mark.parametrize("sequence, result, new_sequence0, new_sequence1", inputData_method1)
def test_method_1(sequence, result, new_sequence0, new_sequence1):
    assert minimum_quantity_of_changes(sequence) == (result, new_sequence0) or (result, new_sequence1)


inputData_method2 = [([], 'please put a non empty sequence as input'), ([0, 1, 5, 0], 'please put a sequence of of coin flips with 0,1 elements')]


@pytest.mark.parametrize("sequence, result", inputData_method2)
def test_method_2(sequence, result):
    assert minimum_quantity_of_changes(sequence) == result








