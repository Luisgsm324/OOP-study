"""
Existem certos métodos que, para a construção de um determinado código, relacionam-se 
com a classe e não necessariamente com o objeto. Para esses métodos, existe uma diferença na sua declaração 
como pode ser notado no exemplo abaixo.
"""

def Pet():
    quantify_pets = 0 # Trata-se de uma variável associada a classe, não ao objeto. 

    def __init__(self, name):
        # Aqui estarão apenas os atributos associados ao objeto, que serão diferentes do de outro objeto
        self.name = name

    # Para criar um método da classe, utiliza a estrutura com @
    @classmethod
    def add_pet(cls): # Utiliza o cls
        cls.quantify_pets += 1

# Segue um exemplo de como poderia ser o uso desse método da classe: 
"""
def Pet():
    quantify_pets = 0 # Trata-se de uma variável associada a classe, não ao objeto. 

    def __init__(self, name):
        # Aqui estarão apenas os atributos associados ao objeto, que serão diferentes do de outro objeto
        self.name = name
        Pet.add_pet()

    # Para criar um método da classe, utiliza a estrutura com @
    @classmethod
    def add_pet(cls): # Utiliza o cls
        cls.quantify_pets += 1
""" 

# Para chamar um método associado a classe, basta fazer igual ao objeto, sendo que referenciando-se ao nome da classe. 