from base64 import encode


class Arte():
    lista_artes = []
    def __init__(self, id, nome, obra):
        self.id = id
        self.__nome = nome
        self.__obra = obra

    # def showArt(self, i):
    #         f = open("pinturas.txt", "r").read() 
    #         separe = f.replace('\n', '')
    #         teste=separe.split(";")    
    #         word = str(teste).split("#") 

    #         for i in word:
    #             print(i, end='')

    @property
    def show(self):
        with open('pinturas.txt', 'r') as arquivo:
            for i in arquivo:
                print(i, end='')

    @property
    def artAdd(self):
        return self.__nome, self.__obra

    #@artAdd.setter
    def artAdd(self, id, new, new2):
        self.__nome = new
        self.__obra = new2
        with open('pinturas.txt', 'a', encoding='utf-8') as p:
            while True:
                p.write("\n"+str(id)+""+" "+new+":"+"\n"+new2+";"+"\n")
                p.close()
                print('ARTE ADICIONADA COM SUCESSO!')

class idArt:
    id = 1
    def set_id(self):
        id += 1
        return id