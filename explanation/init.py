"""
Agora utilizaremos esse arquivo para a criação dos atributos de uma determinada classe. Os atributos seriam
certas "informações" acerca do objeto. Em outras palavras, digamos que você está fazendo registros de alunos, 
um aluno possui nome, idade, turma entre outras informações e, em vez de você criar várias variáveis para cada, 
basta considerar que esses são os atributos do estudante.
"""

class Student():
    def __init__(self, name, age, classroom):
        # O nome não precisa ser igual, então você poderia colocar outra coisa em vez de repetir. 
        self.name = name
        self.age = age
        self.classroom = classroom

"""
Com o caso demonstrado a seguir, criamos uma classe que possui 3 objetos, então quando o objeto for criado
é necessário que se tenha 3 atributos representando o seu nome, idade e turma. A função __init__ também é chamada de 
Constructor por conta da sua função de construir os atributos do objeto. 
"""
student1 = Student("Luis", 18, "E213")
# Você pode printar os atributos fazendo o passo abaixo
print(student1.name)
print(student1.age) 
print(student1.classroom)  

