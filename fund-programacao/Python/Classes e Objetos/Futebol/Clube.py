class Clube:
    def __init__(self, nome, verba):
        self.nome = nome
        self.__jogadores = []
        self.__verba = verba

    @property
    def verba(self):
        return self.__verba
    @verba.setter
    def verba(self, valor, operacao):
        if operacao == 1:
            self.__verba += valor
        if operacao == 2:
            self.__verba -= valor

    @property
    def jogadores(self):
        return self.__jogadores
    @jogadores.setter
    def jogadores(self, jogador):
        self.__jogadores.append(jogador)