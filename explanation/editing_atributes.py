"""
Pegando a classe Student construída no arquivo de init, vamos editar os valores do atributo de uma maneira bem simples. 
Para isso, é necessário que se crie um método que seja capaz de fazer isso (de maneira mais organizada)
"""
class Student():
    def __init__(self, name, age, classroom):
        # O nome não precisa ser igual, então você poderia colocar outra coisa em vez de repetir. 
        self.name = name
        self.age = age
        self.classroom = classroom
    def modify_age(self, age):
        self.age = age

student1 = Student("Luis", 18, "E231")
# Antes da modificação
print(student1.age)

student1.modify_age(20)
# Depois da modificação
print(student1.age)

"""
Essa capacidade de poder alterar atributos facilita em muito o processo de manipulação das informações,
principalmente em trabalhos de larga escala.  
"""