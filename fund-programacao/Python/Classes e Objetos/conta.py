from cliente import *

class Conta:
    cod_banco = 313
    def __init__(self, num, tit, sal, lim):
        print(f'Construindo uma conta nova em {self}')
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
    
    @staticmethod
    def get_cod_banco():
        return __class__.cod_banco
    
    # def set_cliente(self, num):
    #     self.__numero = num
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def set_deposita(self, valor):
        self.__saldo += valor
        
    def __pode_sacar(self, valor):
        return True if valor <- self.__saldo + self.__limite else False
    
    def set_saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Excedeu o limite!")
        
    def set_transfere(self, valor, destino):
        self.set_saca(valor)
        destino.set_deposita(valor)
        

if __name__ == "__main__":
    conta_junin = Conta(23, "junin", 10000, 50000) 
    conta_ooo = Conta(24, "ooo", 20000, 50000)
    
    #conta_junin.set_saca(200000)
    conta_ooo.set_transfere(200, conta_junin)
    print(conta_ooo.get_saldo)
    # print(conta_junin.extrato())
    # conta_junin.deposita(5000.0)
    # print(conta_junin.extrato())
    # conta_ooo.saca(4000.0)
    # print(conta_ooo.saldo)
    