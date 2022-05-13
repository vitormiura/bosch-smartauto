from Arte import *
from Avaliacao import *
import sys


def print_menu():
    print("\033[95m{----NFT MONKEYS----}\033[00m")

    print("1 - Adicionar arte\n"
          "2 - Avaliar arte\n"
          "3 - Exibir avaliações\n"
          "0 - Sair\n")


def op_menu(op):

    if op == 1:
        print("\n\033[92m{----Adicionando Artes----}\033[00m")
        nome = input("Digite o nome da obra: \n")
        obra = input("Inclua a obra: \n")

        id = idArt.id
        id = id + 1
        idArt.id = id

        arte = Arte(id, nome, obra) #instancia
        arte.artAdd(id, nome, obra) #adiciona ao txt
        Arte.lista_artes.append(arte) #append em lista com artes

    elif op == 2:
        print("\n\033[92m{----Avaliando Artes----}\033[00m")
        print("    EXIBIR ARTES AQUI!")

        choose = int(input("Digite o id da obra que deseja avaliar: \n"))
        nome = input("Digite seu nome: ")
        nota = int(input("Dê uma nota para essa arte: \n"))
        feed = input("Digite o Feedback para essa obra: \n")

        avaliacao = Avaliacao(choose, nome, nota, feed) #instancia
        avaliacao.avaAdd(choose, nome, nota, feed) #add ao txt
        Avaliacao.lista_avaliacoes.append(avaliacao) #append em listo com artes


    elif op == 3:
        print("\n\033[92m{----Exibindo Artes/Avaliações----}\033[00m")
        oi = int(input("Digite o id da obra que desejas ver a(s) avaliacao(aos): \n"))

        #arte = Arte(None, None, None)
        #arte.show()
        print("\n")
        avaliacao = Avaliacao(None, None, None, None)
        avaliacao.showAva(oi)
        

    elif op == 0:
        print("\033[93mPrograma Finalizado!\033[00m")
        sys.exit()
    else:
        print("\n\033[91mERRO,DÍGITO INVÁLIDO!!!\033[00m\n")


if __name__ == '__main__':
    while True:
        print_menu()
        try:
            op_user = int(input("Digite a operação desejada: \n"))
            op_menu(op_user)
        except ValueError:
            print("\n\033[91mERRO! DIGITE APENAS NÚMEROS!!!!\n\033[00m")


