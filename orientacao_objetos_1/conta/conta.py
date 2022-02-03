class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        

    # Get
    @property   	
    def numero(self):
        return self.__numero

    @property   	
    def titular(self):
        return self.__titular

    @property   	
    def saldo(self):
        return self.__saldo

    @property   	
    def limite(self):
        return self.__limite


    # Set
    @numero.setter   	
    def numero(self, numero):
        self.__limite = numero

    @titular.setter   	
    def titular(self, titular):
        self.__limite = titular

    @limite.setter   	
    def limite(self, limite):
        self.__limite = limite

    

    # metodo estatico
    @staticmethod   	
    def codigos_bancos():
        return {"BR":"001", "Caixa": "104", "Bradesco": "237"}
    
    
    # metodos 
    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')
    
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

codigos = Conta.codigos_bancos()
print(codigos['BR'])
print(codigos['Caixa'])
print(codigos['Bradesco'])

'''
print(Conta.codigo_banco())


conta = Conta(123, 'Nico', 55.0, 1000.0)
conta.saca(2000.0)
conta.saldo
conta2 = Conta(321, 'Joe', 115.0, 1000.0)
conta.extrato()
conta2.extrato()
conta.transfere(15, conta2)
conta.extrato()
conta2.extrato()

print(conta.numero, conta.titular)
conta.extrato()
conta.saque(10)
conta.extrato()
conta.deposita(100)
conta.extrato()
'''