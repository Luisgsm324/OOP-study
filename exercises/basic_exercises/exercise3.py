"""
Write a Python program to create a calculator class. 
Include methods for basic arithmetic operations.
"""

class Calculator():
    
    @staticmethod
    def sum(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y 
    
    @staticmethod
    def divide(x, y): 
        result = 0
        try: 
            result = x/y 
            return result
        except: 
            return f"Error detectado" 
    
    @staticmethod
    def multiple(x,y): 
        return x * y