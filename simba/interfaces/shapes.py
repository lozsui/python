"""
In here I want to play how interfaces are implemented using Python.
"""

from abc import ABC, abstractmethod
import math

# Shape interface
class ShapeInterface(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Implement the Circle class
class Circle(ShapeInterface):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Implement the Rectangle class
class Rectangle(ShapeInterface):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
