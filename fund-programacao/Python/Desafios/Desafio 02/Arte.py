#import os
#import subprocess
#FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
import Main

class Arte():
    artes_aval = []
    arte_feed = []
    
    def __init__(self, id, name, pint, aval, com, autor, obra):
        self.id = id
        self.__nome = name
        self.__pinturas = pint
        self.__avaliacao = aval
        self.__comentario = com
        self.__autor = autor
        self.__obra = obra
    
    @property
    def pictures(self):
        for i in self.__pinturas:
            print('Pintor da obra: ' + i)
            print(self.__pinturas[i])
        return self.__pinturas
    
    @property
    def arts(self):
        f = open("palavras.txt", "r").read() 
        arte = f.replace('\n', '').split(";")
        
               
    @arts.setter
    def arts(self, autor, obra):
        with open('pinturas.txt', 'a', encoding='utf-8') as p:
            print("-" * 50)
            while True:
                '''self.__autor = input("Digite o artista a ser adicionada: ").lower()
                self.__obra = input(f"Digite a arte do artista ").lower()'''
                
                p.write("\n"+autor+":"+"\n"+obra+";")
                p.close()
                print('ARTE ADICIONADA COM SUCESSO!')
            
    @property
    def identificacao(self):
        return self.id
    
    @property
    def aval(self):
        return "Artista: "+self.__nome+" pintura: "+str(self.__pinturas)+" Avalição: "+self.__avaliacao+\
               " Feedback: "+str(self.__comentario)
               
    @aval.setter
    def aval(self):
        return self
    
    @identificacao.setter
    def identificacao(self):
        self.id = self.id + 1
        return self.id

autor, obra = Main.op_menu

pinturas = Arte("","","","","", autor, obra)
pinturas.arts(autor, obra)