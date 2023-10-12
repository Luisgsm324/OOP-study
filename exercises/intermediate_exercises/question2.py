"""
Crie uma classe chamada Retângulo com os atributos largura e altura. 
Adicione métodos para calcular a área e o perímetro do retângulo. 
Em seguida, crie uma classe derivada chamada Quadrado que herda de Retângulo. 
Sobrescreva os métodos necessários para garantir que um quadrado sempre tenha lados iguais.
"""

class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        area = self.largura * self.altura
        return area
    
    def perimeter(self):
        perimeter = (2*self.largura) + (2*self.altura)
        return perimeter
    
class Quadrado(Retangulo):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def area(self):
        if self.largura == self.altura:
            return super().area()
        return f"O objeto em questão não é um quadrado"
    
    def perimeter(self):
        if self.largura == self.altura:
            return super().perimeter()
        return f"O objeto em questão não é um quadrado"

figura = Quadrado(2,2)
print(figura.area())