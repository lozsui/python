from module1 import nt
from module1 import dc

"""
For details see Fluent Python 2nd edition by Luciano Ramelho.
"""

def test_named_tuple():
    assert issubclass(nt.Coordinate, tuple)

    moscow = nt.Coordinate(lat=55.756, lon=37.617)
    
    assert str(moscow) == 'Coordinate(lat=55.756, lon=37.617)'
    assert moscow == nt.Coordinate(lat=55.756, lon=37.617)


def test_dataclass():
    assert issubclass(dc.Coordinate, object)

    moscow = dc.Coordinate(lat=55.756, lon=37.617)
    
    assert str(moscow) == 'Coordinate(lat=55.756, lon=37.617)'
    assert moscow == dc.Coordinate(lat=55.756, lon=37.617)