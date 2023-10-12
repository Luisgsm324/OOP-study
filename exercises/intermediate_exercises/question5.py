"""
Crie uma classe chamada Loja com os atributos nome, produtos (uma lista de objetos representando produtos) e clientes (uma lista de objetos representando clientes). 
Adicione métodos para adicionar produtos ao estoque, realizar vendas para os clientes (deduzindo os produtos vendidos do estoque) e para calcular o total de vendas de um cliente específico.
"""
        
class Produto():
    def __init__(self, name, price, quantidade):
        self.name = name
        self.price = price
        self.amount = quantidade 

class Cliente():
    def __init__(self, name):
        self.name = name
        self.amount = 0

class Loja:
    def __init__(self, name, products, clients):
        self.name = name
        self.products = products 
        self.clients = clients 

    def add_product(self, product_name, product_price, product_amount):
        for product in self.products:
            if product.name == product_name:
                return f"O produto já está existente na lista de produtos"
        product = Produto(product_name, product_price, product_amount)
        self.products.append(product)
        return f"O produto {product.name} foi adicionado com sucesso!"
        

    def add_client(self, client_name):
        for client in self.clients:
            if client.name == client_name:
                return f"O cliente já está na nossa lista de cadastro!"
        client = Cliente(client_name)
        self.clients.append(client)
        return f"O cliente {client.name} foi cadastrado com sucesso!"

    def sell_product(self, product_name, product_amount, client_name):
        for product in self.products:
            if product.name == product_name: 
                if product.amount >= product_amount: 
                    for client in self.clients:
                        if client.name == client_name:
                            client.amount += (product_amount*product.price)
                            product.amount -= product_amount
                            return f"O cliente {client_name} comprou {product_amount} da loja!"
                    return f"O cliente não se encontra na nossa lista de clientes!"
                return f"A quantidade solicitada é inferior ao que temos no estoque. Não é possível realizar a compra"

    def show_info_client(self, client_name):
        for client in self.clients:
            if client.name == client_name:
                return f"O cliente {client} comprou {client.amount} em reais da loja!"
        return f"O cliente em questão não foi encontrado no banco de dados da loja!"
    
    def show_storage(self):
        string = "Itens no estoque:\n"
        for item in self.products:
            string += f"{item.name} - {item.amount}\n"
        return string

loja = Loja("Mercado", [], [])

while True:
    question = input("O que deseja realizar?\n")

    if question.upper() == "VENDER":
        product_name = input("Informe o nome do produto que você deseja vender: ") # 1
        product_amount = int(input("Insira a quantidade que você deseja vender: ")) # 2
        client_name = input("Informe o nome do cliente que está comprando: ") # 3 
        print(loja.sell_product(product_name, product_amount, client_name))
    
    elif question.upper() == "ADICIONAR CLIENTE":
        client_name = input("Informe o nome do cliente: ")
        print(loja.add_client(client_name))
    
    elif question.upper() == "ADICIONAR PRODUTO":
        product_name = input("Informe o nome do produto que você deseja adicionar: ")
        product_price = int(input("Informe o preço desse produto individualmente: "))
        product_amount = int(input("Insira a quantidade que você deseja adicionar: "))
        print(loja.add_product(product_name, product_price, product_amount))
    
    elif question.upper() == "MOSTRAR ESTOQUE":
        print(loja.show_storage())

    elif question.upper() == "SAIR":
        print("Obrigado por usar nosso sistema!")
        break
        
