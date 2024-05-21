
"""
Documentation on build-in functions: https://docs.python.org/3.12/library/functions.html
"""

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

