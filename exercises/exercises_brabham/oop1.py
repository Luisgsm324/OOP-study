class Individual():
    def __init__(self, name):
        self.character_name = name 

    def get_character_name(self):
        return self.character_name

individual1 = Individual("Buster")
individual2 = Individual("Tobias")

print(individual1.get_character_name())
print(individual2.get_character_name())