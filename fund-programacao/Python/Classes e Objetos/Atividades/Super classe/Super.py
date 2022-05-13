class Animal():
    def __init__(self, fam, esp, ali):
        self.familia = fam
        self.especie = esp
        self.alimenta = ali


class Vaca(Animal):
    def __init__(self, fam, esp, ali, nome, cor):
        super().__init__(fam, esp, ali)
        self.__nome = nome
        self.__coloracao = cor

class Morcego(Animal):
    def __init__(self, fam, esp, ali, nome, asa):
        super().__init__(fam, esp, ali)
        self.__nome = nome
        self.__tamanhoasa = asa

if __name__ == "__main__":

    vaca = Vaca()