"""
Crie uma classe chamada Aluno com os atributos nome, matricula e uma lista de notas. 
Adicione métodos para calcular a média das notas e para adicionar uma nova nota à lista
"""

class Aluno():
    def __init__(self, nome ,matricula, notas):
        self.nome = nome 
        self.matricula = matricula 
        self.notas = notas # É uma lista
    
    def calc_average(self):
        count = 0
        for grade in self.notas:
            count += grade
        average = count/len(self.notas)
        return f"A média do aluno {self.nome} foi {average}"
    
    def add_grade(self, grade):
        self.notas.append(grade)
        return f"A nota {grade} foi adicionada. Lembre-se de recalcular a sua média!"

aluno = Aluno("Lucas", 776, [5,5,5])

print(aluno.calc_average())
print(aluno.add_grade(0))
print(aluno.calc_average())