class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    

    def extrato(self):
        print(f'Saldo {self.saldo} do titular {self.titular}')
    
    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor




conta = Conta(123, 'Nico', 55.0, 1000.0)
print(conta.numero, conta.titular)
conta.extrato()
conta.saque(10)
conta.extrato()
conta.deposita(100)
conta.extrato()
