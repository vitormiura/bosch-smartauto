
class Conta:
    def __init__(self, num, tit, sal, lim):
        print(f'Construindo em {self}')
        self.__numero = num
        self.__titular = tit
        self.__saldo = sal
        self.__limite = lim
    
    def extrato(self):
        print(f'saldo {self.__saldo} reais do titular {self.__titular}.')
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor
        
    def transfere(self, valor, destinho):
        self.saca(valor)
        destinho.depositar(valor)

if __name__ == "__main__":
    conta_junin = Conta(23, "junin", 10000, 50000) 
    conta_ooo = Conta(24, "ooo", 20000, 50000)
    
    conta_ooo.transfere(conta_junin, 200)
    
    # print(conta_junin.extrato())
    # conta_junin.deposita(5000.0)
    # print(conta_junin.extrato())
    # conta_ooo.saca(4000.0)
    # print(conta_ooo.saldo)
    