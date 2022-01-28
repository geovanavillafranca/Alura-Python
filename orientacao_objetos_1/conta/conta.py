class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')
    
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)






conta = Conta(123, 'Nico', 55.0, 1000.0)
conta2 = Conta(321, 'Joe', 115.0, 1000.0)
conta.extrato()
conta2.extrato()
conta.transfere(15, conta2)
conta.extrato()
conta2.extrato()
'''
print(conta.numero, conta.titular)
conta.extrato()
conta.saque(10)
conta.extrato()
conta.deposita(100)
conta.extrato()
'''