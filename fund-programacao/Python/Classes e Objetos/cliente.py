from conta import *

class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, new):
        print("SETTER AQUI")
        self.__nome = new
    
cliente = Cliente("clebinho")
print(cliente.nome)
cliente.nome = "aaa"
print(cliente.nome)
        
