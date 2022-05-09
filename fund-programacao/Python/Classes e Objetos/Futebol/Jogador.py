from ControlaId import ControlaId
#from ListaJogadores import ListaJogadores


class Jogador:
    lista_jogadores = [] #static
    sal_min = 1212.00
    def __init__(self, id, nome, idade, posicao, salario, numero, temClube):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.__salario = salario
        self.numero = numero
        self.temClube = temClube

    def get_salario(self):
        return self.__salario
    
    @staticmethod
    def get_salario_min():
        return Jogador.sal_min
    
    def aumento(self, valor):
        self.__salario += valor
        
    def __reducao(self, valor):
        return True if valor <- Jogador.get_salario_min() else print("Salario ja esta no valor minimo")

    def info(self):
        return "Nome: "+self.nome+" Idade: "+str(self.idade)+" Posicao: "+self.posicao+\
               " Salario: "+str(self.__salario)+" Numero: "+str(self.numero)

