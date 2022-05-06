class Estadio:
    def __init__(self, nome, localizacao, dono):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__dono = dono

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def localizacao(self):
        return self.__localizacao
    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao
    @property
    def dono(self):
        return self.__dono
    @dono.setter
    def dono(self, dono):
        self.__dono = dono