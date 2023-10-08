class Individual():
    count = 0 

    @classmethod
    def Addone(cls):
        cls.count += 1
        return cls.count

    def __init__(self, name):
        self.character_name = name
        self.happy = True
        self.id = Individual.Addone()

    def get_id(self):
        return self.id

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
    
    def info(self):
        return f"individual: [{self.id} {self.character_name}]"


individual1 = Individual("Buster")
individual2 = Individual("Tobias")
individual3 = Individual("Lucille")

print(individual1.info())

print(individual1.get_id())
print(individual2.get_id())
print(individual3.get_id())