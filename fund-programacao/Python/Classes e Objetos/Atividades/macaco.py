class Macaco:
    def __init__(self, n = '', r = '', s = '', t = ''):
        self.__name = n
        self.raca = r
        self.sexo = s
        self.__temperamento = t
        
    @property
    def nome(self):
        return self.__name.title()
    
    def get_raca(self):
        return self.raca 
    def get_sexo(self):
        return self.sexo 
    def get_temp(self):
        return self.__temperamento 

    def set_temp(self, temp):
        self.__temperamento = temp 
        
    @nome.setter
    def nome(self, new):
        self.__name = new
        
if __name__ == "__main__":
    
    Macaco.sexo = ['M', 'F']
    
    macaco1 = Macaco('', 'chimp', Macaco.sexo[0], 'docil')
    
    macaco1.nome= "Cezar"
    macaco1.set_temp("Maduro")
    
    print(macaco1.nome)
    print(macaco1.get_raca())
    print(macaco1.get_sexo())
    print(macaco1.get_temp())