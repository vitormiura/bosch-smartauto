class Zoo:
    def __init__(self, loc = "", ani = '', esp = '', cu = '', ca = ''):
        self.__local = loc
        self.__qtd_animal = ani
        self.__qtd_especie = esp
        self.__qtdcuidador = cu
        self.__capacidade = ca
        
    
    def get_loc(self):
        return self.__local
    def get_ani(self):
        return self.__qtd_animal
    def get_esp(self):
        return self.__qtd_especie
    def get_cuida(self):
        return self.__qtdcuidador
    def set_capa(self):
        return self.__capacidade
    
    def set_ani(self, new):
        self.__qtd_animal = new
    def set_esp(self, new):
        self.__qtd_especie = new
    def set_cuida(self, new):
        self.__qtdcuidador = new
        

if __name__ == "__main__":
    aaa = Zoo('Campinas', 150, 46, 10, 3000)
    
    l = []
    aaa.append[l]
    print(l)
    
    
    
    
    
