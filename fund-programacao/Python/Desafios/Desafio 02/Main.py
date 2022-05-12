from Arte import *

def print_menu():
    print("\033[95m{----NFT MONKEYS----}\033[00m")

    print("1 - Adicionar arte\n"
          "2 - Avaliar arte\n"
          "3 - Exibir avaliações\n"
          "0 - Sair\n")


def op_menu(op):

    if op == 1:
        print("\n\033[92m{----Adicionando Artes----}\033[00m")
        autor = input("Digite o nome do autor: \n")
        obra = input("Digite o nome da obra: \n")

        return autor, obra

    elif op == 2:
        print("\n\033[92m{----Avaliando Artes----}\033[00m")
        print("    EXIBIR ARTES AQUI!")
        escolha = int(input("Escolha a arte que deseja avaliar: \n"))
        nota = int(input("Dê uma nota para essa arte: \n"))
        return escolha, nota

    elif op == 3:
        print("\n\033[92m{----Exibindo Artes/Avaliações----}\033[00m")
        mostrar_arte = int(input("Qual obra deseja exibir? \n"))
        return mostrar_arte
    elif op == 0:
        print("\033[93mPrograma Finalizado!\033[00m")
        exit()
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


