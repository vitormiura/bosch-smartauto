class Avaliacao():
    lista_avaliacoes = []
    def __init__(self, nome, id, nota, feed):
        self.id = id
        self.__nome = nome
        self.__nota = nota
        self.__feedback = feed
        
    
    def showAva(self, a):
            f = open("ava.txt", "r").read() 
            separe = f.replace('\n', '')
            teste=separe.split("#")    
            #word = str(teste).split("#") 
            #print(teste)
            #word = str(teste).split(";")
            kk = str(a)

            cont = -1
            for i in teste:
                cont = cont + 1
                if i == kk:
                    word = str(teste).split(";")
                    print(teste[cont + 1])
                



    @property
    def avaAdd(self):
        return self.__nome, self.__nota, self.__feedback

    #@avaAdd.setter
    def avaAdd(self, id, new, new2, new3):
        self.__nome = new
        self.__nota = new2
        self.__feedback = new3
        with open('ava.txt', 'a', encoding='utf-8') as a:
            while True:
                a.write("\n"+"#"+str(id)+"#"+" "+new+":"+str(new2)+","+ new3+";")
                a.close()
                print('AVALIACAO ADICIONADA COM SUCESSO!')
    

# class idAva:
#     id1 = 1
#     def set_id(self):
#         id1 += 1
#         return id1