# -*- coding: utf-8 -*-

"""
No comment.
"""

from dataclasses import asdict
import classes.bits_n_bobs as bb

def test_dog_class():
    my_dog = bb.Dog(name="Yoy", sex="f")
    my_dog_dict = asdict(my_dog)
    assert my_dog_dict["name"] == "Yoy"