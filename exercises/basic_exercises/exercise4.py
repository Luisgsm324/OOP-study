"""
Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like circle, triangle, and square.
"""

class Shape(): 
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class Circle(Shape):
    def __init__(self, value1, value2): # Valor do Raio e de Pi
        super().__init__(value1, value2)
    
    def area(self): 
        area = (self.value1**2)*self.value2
        return area 
    
    def perimeter(self): 
        return 2*self.value2*self.value1
    
class Rectangle(Shape): 
    def __init__(self, value1, value2): # Largura e comprimento
        super().__init__(value1, value2)
    
    def area(self): 
        area = self.value1*self.value2
        return area 
    
    def perimeter(self): 
        perimeter = 2*self.value1 + 2*self.value2
        return perimeter 

class Triangle(Shape):
    def __init__(self, value1, value2, value3): # Base, altura e lado que restou
        super().__init__(value1, value2)
        self.value3 = value3
    
    def area(self):
        area = (self.value1*self.value2)/2
        return area
    
    def perimeter(self):
        perimeter = self.value1 + self.value2 + self.value3
        return perimeter 


triangle = Triangle(3,4,5)
print(triangle.area())

"""
Resolução do site: 

import math
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
"""