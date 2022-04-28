class Macaco:
    def __init__(self, n = '', r = '', s = '', t = ''):
        self.__name = n
        self.__raca = r
        self.sexo = s
        self.__temperamento = t
        
    def get_name(self):
        return self.__name
    def get_raca(self):
        return self.__raca 
    def get_sexo(self):
        return self.sexo 
    def get_temp(self):
        return self.__temperamento 
    
    def set_name(self, nome):
        self.__name = nome
    def set_temp(self, temp):
        self.__temperamento = temp 
        
if __name__ == "__main__":
    Macaco.sexo = ['M', 'F']
    
    cesar = Macaco('antonio', 'chimp', Macaco.sexo[0], 'zaralhado')
    
    cesar.set_name("César")
    cesar.set_temp("Maduro")
    
    print(cesar.get_name())
    print(cesar.get_raca())
    print(cesar.get_sexo())
    print(cesar.get_temp())