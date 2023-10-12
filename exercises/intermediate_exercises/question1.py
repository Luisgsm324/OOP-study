"""
Crie uma classe chamada Animal com os métodos emitir_som() e movimentar(). 
Em seguida, crie duas classes derivadas de Animal chamadas Cachorro e Pássaro. 
Implemente os métodos emitir_som() de forma diferente para cada classe derivada.
"""

class Animal():
    def emitir_som(self):
        return f"Som do animal!!"
    
    def movimentar(self):
        return f"O animal está se movimentando"

class Cachorro(Animal):
    def emitir_som(self):
        return f"Au au!"

class Passaro(Animal):
    def emitir_som(self):
        return f"Piu Piu"
    
animal = Cachorro()
print(animal.emitir_som())