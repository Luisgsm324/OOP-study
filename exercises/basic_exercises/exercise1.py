"""
Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter.
"""

class Circle():
    def __init__(self, radius, pi_value):
        self.radius = radius
        self.pi_value = pi_value
    
    def perimeter(self):
        return (2*self.pi_value*self.radius)

    def area(self):
        return self.pi_value*(self.radius**2)

 