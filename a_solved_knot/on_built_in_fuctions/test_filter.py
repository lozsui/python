from collections import namedtuple

def positive(arg: int) -> bool:
    if arg > 0:
        return True
    if arg < 0:
        return False

def test_postive_ints():
    postive = list(filter(positive, [-1, 23, -42, 1291]))
    assert 23 in postive
    assert 1291 in postive

def taller_than(person) -> bool:
    if person.height > 190:
        return True
    else:
        return False

def test_human_bigger_than():
    Person = namedtuple("Person", "name height")
    persons = [
        Person("Otto", 160),
        Person("Werner", 190),
        Person("Herrmann", 192),
    ]
    tall_persons = list(filter(taller_than, persons))
    assert Person("Herrmann", 192) in tall_persons
    assert Person("Otto", 160) not in tall_persons