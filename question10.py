from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Create instances of Circle and Square and call area()
circle = Circle(5)
square = Square(4)

print(f"Area of the circle: {circle.area():.2f}")  # Circle with radius 5
print(f"Area of the square: {square.area()}")     # Square with side 4
