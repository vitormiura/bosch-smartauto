class Arte():
    lista_artes = []
    def __init__(self, id, nome, obra):
        self.id = id
        self.__nome = nome
        self.__obra = obra

    # @property
    # def pictures(self):
    #     for i in self.__pinturas:
    #         print('Nome da obra: ' + i)
    #         print(self.__pinturas[i])
    #     return self.__pinturas

    # @property
    # def artAdd(self):
    #     f = open("palavras.txt", "r", encoding='utf-8').read() 
    #     arte = f.replace('\n', '').split(",")
    @property
    def artAdd(self):
        return self.__nome, self.__obra

    @artAdd.setter
    def artAdd(self, id, new, new2):
        self.__nome = new
        self.__obra = new2
        with open('pinturas.txt', 'a', encoding='utf-8') as p:
            while True:
                p.write("\n"+id +new+":"+"\n"+new2+",")
                p.close()
                print('ARTE ADICIONADA COM SUCESSO!')

class idArt:
    id = 1
    def set_id(self):
        id += 1
        return id