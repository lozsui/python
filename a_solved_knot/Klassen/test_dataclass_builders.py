from Klassen.dataclass_builders import NamedTupleDog, DataclassDog
from dataclasses import asdict
from collections import namedtuple

"""
Siehe auch Kapitel 5 'Data Class Builders' in Fluent Python von Luciano Ramelho.
"""

def test_named_tuple_from_collections():
    Dog = namedtuple('Dog', 'name sex')
    assert issubclass(Dog, tuple)
    yoy = Dog(name="Yoy", sex="f")
    assert str(yoy) == "Dog(name='Yoy', sex='f')"
    assert yoy == Dog(name="Yoy", sex="f")


def test_named_tuple_from_typing():
    assert issubclass(NamedTupleDog, tuple)

    yoy = NamedTupleDog(name="Yoy", sex="f")
    assert yoy.name == "Yoy"
    
    assert str(yoy) == "NamedTupleDog(name='Yoy', sex='f')"
    assert yoy == NamedTupleDog(name="Yoy", sex="f")


def test_dataclass():

    assert issubclass(DataclassDog, object)

    yoy = DataclassDog(name="Yoy", sex="f")
    assert yoy.name == "Yoy"
    
    assert str(yoy) == "DataclassDog(name='Yoy', sex='f')"
    assert yoy == DataclassDog(name="Yoy", sex="f")

    dog_as_dict = asdict(yoy)
    assert dog_as_dict["name"] == "Yoy"
