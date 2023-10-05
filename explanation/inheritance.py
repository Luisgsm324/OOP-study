"""
Basicamente, quando tivermos classes que são muito semelhantes entre si,
podemos utilizar a herança para facilitar nosso trabalho, permitindo que uma 
"adote" a outra como o seu filho, permitindo o acesso aos atributos e métodos 
da classe adotada como "pai". 
"""

class Pet():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")

class Cat(Pet): # Para herdar os atributos e métodos da classe basta colocar a classe como o parâmetro
    def speak(self):
        print("Meow")

pet = Pet("George", 18)
pet.show()

cat = Cat("Stewart", 20)
cat.speak()
cat.show()

"""
Hipoteticamente, se você criasse um método para a classe "pai" com o mesmo nome que o "filho",
o método do filho vai se sobressair já que ele foi declarado posteriormente. 
Outro ponto seria acerca da utilização do super().__init__() que pegará os atributos desejados por você 
"""

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # Precisamos referenciar para saber quais são os atributos a serem chamados.

dog = Dog("Cleiton", 24)
dog.show()