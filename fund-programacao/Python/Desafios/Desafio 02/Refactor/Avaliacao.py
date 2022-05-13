class Avaliacao():
    lista_avaliacoes = []
    def __init__(self, nome, id, nota, feed):
        self.id = id
        self.__nome = nome
        self.__nota = nota
        self.__feedback = feed
        
    @property
    def avaAdd(self):
        f = open("palavras.txt", "r", encoding='utf-8').read() 
        arte = f.replace('\n', '').split(",")

    @avaAdd.setter
    def avaAdd(self, id, nome, nota, feed):
        with open('avaliacoes.txt', 'a', encoding='utf-8') as p:
            while True:
                p.write("\n"+id +nome+":"+nota+","+ feed+",")
                p.close()
                print('AVALIACAO ADICIONADA COM SUCESSO!')
    











class idAva:
    id1 = 1
    def set_id(self):
        id1 += 1
        return id1
    
