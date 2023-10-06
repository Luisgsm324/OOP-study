"""
Write a Python program to create a person class. Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.
"""
import time
class Person():
    
    def __init__(self, name, country, birth):
        self.name = name 
        self.country = country
        self.birth = birth
    
    def determine_age(self):
        dates = self.birth.split("-")
        age = time.localtime()[0] - int(dates[0]) 
        if int(dates[1]) <= time.localtime()[1]:
            if int(dates[2]) <= time.localtime()[2]:
                return age
            return age - 1
        return age - 1

person1 = Person("George", "Brazil", "2001-10-4")
print(person1.determine_age())

"""
Solução do site: 

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

Não sabia muito bem como utilizar a biblioteca time, apesar de saber que o uso dela seria necessário. Peguei a primeira função e fui me virando com ela
mas vi que tinha uma forma bem mais otimizada de fazer e com menos identação. 
"""