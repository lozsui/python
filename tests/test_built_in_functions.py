"""
Documentation on build-in functions: https://docs.python.org/3.12/library/functions.html
"""

import os
import pytest

@pytest.mark.parametrize("expected_lines, test_file_path", [
    (
        [
            "Hello,\n",
            "My name is Hermann.\n",
            "Bye\n",
        ],
        'input_iter_test.txt'
    ),
    # Add more parameter here if needed.
])

# TODO: Investigate why I FileNotFoundError is raised.
def _test_iter(expected_lines, test_file_path):
    os.chdir('./files')
    current_working_dir = f"\n Current working directorey is {os.getcwd()}.\n"
    print(current_working_dir)
    with open(test_file_path, 'r') as file:
        for expected_line, line_read in zip(expected_lines, iter(file.readline, '')):
            assert expected_line == line_read


def test_abs():
    my_int = -20
    assert 20 == abs(my_int)
    my_float = 3.141
    assert 3.141 == abs(my_float)
    my_complex = 3 + 4j
    assert 5.0 == abs(my_complex)


def test_len():
    my_list = [0 , 1, 2]
    assert len(my_list) == 3
    my_str = "Sam"
    assert len(my_str) == 3
    my_dict = {}
    assert len(my_dict) == 0
    my_dict["key"] = "value"
    assert len(my_dict) == 1
    my_dict["key"] = {}
    assert len(my_dict) == 1
    my_dict["key"]["subkey1"] = "value 1"
    assert len(my_dict) == 1
    my_dict["key"]["subkey2"] = "value 2"
    assert len(my_dict) == 1
    my_sub_dict = my_dict["key"]
    assert len(my_sub_dict) == 2

