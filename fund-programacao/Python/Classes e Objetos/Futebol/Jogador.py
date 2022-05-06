from ControlaId import ControlaId
#from ListaJogadores import ListaJogadores


class Jogador:
    ListaJogadores = [] #estatico
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


    def aumento(self, valor):
        self.__salario += valor
    def reducao(self, valor):
        self.__salario -= valor
    def info(self):
        return "Nome: "+self.nome+" Idade: "+str(self.idade)+" Posicao: "+self.posicao+\
               " Salario: "+str(self.__salario)+" Numero: "+str(self.numero)

