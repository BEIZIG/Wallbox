import os
import re
import pytest
from functions import first_file_meets_the_requirement
# ************************generate input data************************
path1 = ".\\input1"
path2 = ".\\input2"
file_type = 'exe'
size = 14680064
input_data_1 = [(path1, file_type, size, 'test1')]
input_data_2 = [(path2, file_type, size, None)]


# ********************************test cases********************************
# Positive test case
@pytest.mark.parametrize("path, file_type, size, result", input_data_1)
def test_method_1(path, file_type, size, result):
    assert first_file_meets_the_requirement(path, file_type, size) == result

# Negative test case
@pytest.mark.parametrize("path, file_type, size, result", input_data_2)
def test_method_2(path, file_type, size, result):
    assert first_file_meets_the_requirement(path, file_type, size) == result
