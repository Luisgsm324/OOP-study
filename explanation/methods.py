"""
Métodos sendo criados na classe, podemos criar diversos e para chamar esse método basta colocar
o objeto acompanhado de um . e o nome desse método, como é no caso do objeto maggie. 
"""

class Dog:
    def bark(self):
        print("Au!")
    
    # Podem existir múltiplos métodos em uma classe, basta escrever corretamente :)
    def sleep(self):
        print("Maggie está dormindo no momento")

maggie = Dog()
# Você nota que em vez dele printar int, str, float ou bool ele informa __main__.Dog, mostrando a classe pela qual o objeto é representado.
print(type(maggie))
maggie.bark()
maggie.sleep()
