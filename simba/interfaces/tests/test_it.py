from shapes import (Rectangle, Circle, ShapeInterface)

def test_rectangle_is_shape_subtype():
    my_rectangle = Rectangle(3, 4)
    assert isinstance(my_rectangle, ShapeInterface)

def test_rectangle_area():
    my_rectangle = Rectangle(3, 4)
    assert 12 == my_rectangle.area()

def test_circle_perimeter():
    my_circle = Circle(5)
    assert 31.41592653589793 == my_circle.perimeter()
