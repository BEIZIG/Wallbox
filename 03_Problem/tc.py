import random
import pytest
from functions import minimum_quantity_of_changes
# ************************methods to generate test data************************
def generate_interspersed_sequence(x):
    sequence = []
    start = random.randint(0, 1)
    sequence.append(start)
    for i in range(x):
        sequence.append(1-sequence[i])
    return sequence

def insert_n_modification(x,n):
    already_used = []
    sequence = generate_interspersed_sequence(x)
    for i in range(n):
        p = random.randint(0, x)
        while p in already_used:
            p = random.randint(0, x)
        sequence[p] = (1-sequence[p])
        already_used.append(p)
    return sequence
# ********************************test cases********************************
# data driven test
x = random.randint(3, 10)
#in this case we have interspersed_sequence we expect to have 0 as result
sequence1 = generate_interspersed_sequence(x)
inputData1 = (sequence1, 0)
#in this case we have a sequence of one element we expect to have 0 as result
sequence2 = [random.randint(0, 1)]
inputData2 = (sequence2, 0)
#in this case we have non interspersed_sequence with modification < x/2 we expect to have p as result
p = random.randint(1, int(x/2)-1)
sequence3 = insert_n_modification(x, p)
inputData3 = (sequence3, p)
#in this case we have non interspersed_sequence with modification > x/2 we expect to have x-p-+1 as result
p = random.randint(int(x/2)+1, x)
sequence4 = insert_n_modification(x, p)
inputData4 = (sequence4, x-p+1)
inputData = [inputData1, inputData2, inputData3, inputData4]

@pytest.mark.parametrize("sequence,result",inputData)
def test_method_1(sequence, result):
    assert minimum_quantity_of_changes(sequence) == result







