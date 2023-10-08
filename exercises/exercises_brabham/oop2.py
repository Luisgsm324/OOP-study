class Individual():
    def __init__(self, name):
        self.character_name = name
        self.happy = True

    def is_happy(self):
        return self.happy 
    
    def switch_mod(self):
        if self.happy: 
            self.happy = False
            return self.happy
        return self.happy
    
    def speak(self):
        if self.happy: 
            return f"Hello, I am {self.character_name}"
        return "Go away"

    def get_character_name(self):
        return self.character_name

individual1 = Individual("Buster")
individual2 = Individual("Tobias")
individual3 = Individual("Lucille")

# Alguns testes!
print(individual3.speak())
print(individual3.is_happy())
individual3.switch_mod()
print(individual3.speak())
print(individual3.is_happy())