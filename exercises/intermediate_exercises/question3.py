"""
Crie uma classe chamada ContaBancaria com os atributos saldo, numero_conta e titular. 
Adicione métodos para depositar, sacar dinheiro da conta e para exibir o saldo. 
Implemente um método para verificar se há saldo suficiente antes de efetuar um saque.
"""

class ContaBancaria():
    def __init__(self, saldo, numero_conta, titular):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.titular = titular
    
    def deposit(self, amount):
        self.saldo += amount
        return f"Adicionado {amount} para a conta {self.numero_conta}. O total ficou {self.saldo}"

    def withdraw(self, amount):
        if amount > self.saldo:
            return f"Operação não pode ser realizada, pois o saldo é insuficiente pela quantidade que você deseja sacar!"
        self.saldo -= amount
        return f"Retirado {amount} da conta {self.numero_conta}. O total ficou {self.saldo}"

conta = ContaBancaria(200, 776, "Luis")

while True:
    question = input("O que deseja realizar?\n")

    if question.upper() == "DEPOSITAR":
        deposit_amount = int(input("Insira a quantia que deseja depositar: "))
        print(conta.deposit(deposit_amount))
    
    elif question.upper() == "SACAR":
        withdraw_amount = int(input("Insira a quantidade que deseja sacar: "))
        print(conta.withdraw(withdraw_amount))
    
    elif question.upper() == "SAIR":
        print("Obrigado por usar nosso sistema!")
        break


