from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print(f"Площадь круга: {circle.area():.2f}")
print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Площадь треугольника: {triangle.area()}")
