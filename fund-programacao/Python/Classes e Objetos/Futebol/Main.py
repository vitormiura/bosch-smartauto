import sys
from Clube import Clube
from ControlaId import ControlaId
from ControlaIdClube import idClube as idC
from Jogador import Jogador
#from ListaJogadores import ListaJogadores
#from ListaClubes import ListaClubes


def main():
    controlador = True
    # jogador = Jogador("Ricardo", 22, "Centro avante", 3000, 12)
    # clube = Clube("Palmeiras", 200000)

    while controlador:
        print("-"*20)
        print("PAINEL")
        print("1-Inserir jogador em clube")
        print("2-Cadastrar novo jogador")
        print("3-Trazer informações de jogador")
        print("4-Lista de jogadores sem clube")
        print("5-Criar novo clube")
        print("6-Sair do programa")


        op = int(input("Escolha a opção desejada: "))

        if op == 1:
            id = int(input("Digite o ID do jogador: "))
            if id in Jogador.lista_jogadores:
                jogador = Jogador.lista_jogadores[id - 1] 
                Clube.jogadores.setter(jogador)
                
            else:
                print('id nao existente')

            # idClube = int(input("Digite o ID do seu clube: "))
            # clube = Clube.lista_clubes[idClube-1]
            # print(clube)

        if op == 2:
            nome = input("Digite o nome do jogador: ")
            idade = int(input("Digite a idade do jogador: "))
            posicao = input("Digite a posição do jogador: ")
            salario = input("Digite o salário do jogador: ")
            numero = int(input("Digite o número do jogador: "))
            clubeBool = input("O jogador tem clube? (S/N): ")

            if(clubeBool.upper() == "S"):
                clubeBool = True
            else:
                clubeBool = False

            id = ControlaId.id
            id = id + 1
            ControlaId.id = id
            jogador = Jogador(id, nome, idade, posicao, salario, numero, clubeBool)

            #ListaJogadores.lista_jogadores.append(jogador)
            Jogador.lista_jogadores.append(jogador)

        if op == 3:
            id = int(input("Digite o ID do jogador: "))
            if id in Jogador.lista_jogadores:
                jogador = Jogador.lista_jogadores[id - 1]
                print(jogador.info())
            else: 
                print("ID do jogador não encontrado")            

        if op == 4:
            for i in Jogador.lista_jogadores:
                if i.temClube == False:
                    print(i)
                    
        if op == 5:
            club = input("Digite o nome do novo clube: ")
            verba = int(input("Digite o verba disponivel do clube: "))
            
            id = idC.id
            id = id + 1
            idC.id = id
            
            clube = Clube(club, verba)
            # ListaClubes.lista_clubes.append(clube)
            Clube.lista_clubes.append(clube)
        
        if op == 6:
            sys.exit()

main()


