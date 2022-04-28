from cliente import *

class Conta:
    def __init__(self, num, tit, sal, lim):
        print(f'Construindo em {self}')
        self.__numero = num
        self.__titular = tit
        self.__saldo = sal
        self.__limite = lim
    
    # def extrato(self):
    #     print(f'saldo {self.__saldo} reais do titular {self.__titular}.')
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def set_cliente(self, num):
        self.__num = num
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def set_deposita(self, valor):
        self.__saldo += valor
    
    def set_saca(self, valor):
        self.__saldo -= valor
        
    def set_transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        

if __name__ == "__main__":
    conta_junin = Conta(23, "junin", 10000, 50000) 
    conta_ooo = Conta(24, "ooo", 20000, 50000)
    
    conta_junin.set_saca(200)
    conta_ooo.set_transfere(200, conta_junin)
    
    # print(conta_junin.extrato())
    # conta_junin.deposita(5000.0)
    # print(conta_junin.extrato())
    # conta_ooo.saca(4000.0)
    # print(conta_ooo.saldo)
    