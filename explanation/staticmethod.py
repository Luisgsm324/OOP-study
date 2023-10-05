"""
Quando falamos de métodos estáticos estes estão relacionados ao conjunto de funções associadas a uma temática específica que são agrupadas, 
tornando estáticas e apenas utilizadas para melhorar a organização do código (não apenas utilizadas para isso, porém compreende-se melhor dessa forma).
Esses métodos estáticos criados podem ser utilizados semelhantes ao uso de uma biblioteca externa, como o pygame, sys, opencv e outras. 
"""

class Math: 
    @staticmethod 
    def sum(x, y): # Não é necessário colocar cls ou self, já que são métodos estáticos
        return x + y

print(Math.sum(5, 2))