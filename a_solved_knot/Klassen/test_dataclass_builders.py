from Klassen.dataclass_builders import NamedTupleDog, DataclassDog
from dataclasses import asdict


"""
For details see Fluent Python 2nd edition by Luciano Ramelho.
"""

def test_named_tuple():
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
