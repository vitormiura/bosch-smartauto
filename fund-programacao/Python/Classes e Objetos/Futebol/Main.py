from Clube import Clube
from ControlaId import ControlaId
from Jogador import Jogador
from ListaJogadores import ListaJogadores


def main():
    controlador = True
    # jogador = Jogador("Ricardo", 22, "Centro avante", 3000, 12)
    clube = Clube("Palmeiras", 200000)

    while controlador:
        print("-"*20)
        print("PAINEL")
        print("1-Inserir jogador em clube")
        print("2-Cadastrar novo jogador")
        print("3-Trazer informações de jogador")
        print("4-Lista de jogadores sem clube")
        print("5-Criar novo clube")
        print("6-Sair do programa")


        opcao = int(input("Escolha a opção desejada: "))

        if opcao == 1:
            id = int(input("Digite o ID do jogador: "))

            jogador = ListaJogadores.lista_jogadores[id - 1]
            print(jogador)

            idClube = int(input("Digite o ID do seu clube: "))


        if opcao == 2:
            nome = input("Digite o nome do jogador: ")
            idade = int(input("Digite a idade do jogador: "))
            posicao = input("Digite a posição do jogador: ")
            salario = input("Digite o salário do jogador: ")
            numero = int(input("Digite o número do jogador: "))
            clubeBool = input("O jogador tem clube?S/N: ")

            if(clubeBool.upper() == "S"):
                clubeBool = True
            else:
                clubeBool = False

            id = ControlaId.id
            id = id + 1
            ControlaId.id = id
            jogador = Jogador(id, nome, idade, posicao, salario, numero, clubeBool)

            ListaJogadores.lista_jogadores.append(jogador)

        if opcao == 3:
            id = int(input("Digite o ID do jogador: "))
            jogador = ListaJogadores.lista_jogadores[id - 1]
            print(jogador.info())
        if opcao == 4:
            for i in ListaJogadores.lista_jogadores:
                if i.temClube == False:
                    print(i)
                    
        #if opcao == 5:
            
main()


