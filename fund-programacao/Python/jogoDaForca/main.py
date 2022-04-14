import random
import time
import sys
from macacos import *


def main():

    print('Jogo da Forca!')
    time.sleep(0.5)
    op = input('Deseja Iniciar? (S/N)').lower()

    if op == 's':
        game()
    else:
        sys.exit()

def acerto(index, list, letra):
    print("Acertou a letra!")
    list[index] = letra
    return list

def win():
    op = input("Ganhou! queres jugar dnv?(s/n) ").lower()
    if op == 's':
        main()
    elif op == 'n':
        exit()
    else:
        print('op nao e valida!')
        win()
        
def errou():
    op = input("errou amigo, queres jugar dnv?(s/n) ").lower()
    if op == 's':
        main()
    elif op == 'n':
        exit()

    else:
        print("Opção inválida!")
        errou()

def game():

    print('Sorteando a palavra...')

    f = open("palavras.txt", "r").read()
    row_arr = f.replace('\n', '').split(";")   
    randow_row = row_arr[random.randint(0, len(row_arr)-1)]  
    palavras = randow_row.split(":")[0]    
    dica = randow_row.split(":")[1]
        
        # palavras = arch.read()
        # palavras = palavras.split(";").index[0]
        # dica = palavras.split(":").index[1]

    palavra = random.choice(palavras)
    ind = palavras.index(palavra)
    tam = len(palavra)

    global erroG
    erroG = 0

    print(f'A palavra sorteada tem {tam} letras')

    print(f'Dica -> {dica}')

    lp = []
    ll = []

    for i in range(tam):
        lp.append("_")

    print(macacoBraco2)
    print(''.join(lp))

    for i in range(10):
        letra = input("Chute uma letra: ")
        erro = 0
        acerto = 0

        for u in range(len(palavra)):
            if letra == palavra[u]:
                ind = u
                lp = acerto(ind, list, letra)
                acerto += 1
                print(macacoInteiro)
                print(''.join(lp))

            else:
                ll.append(letra)
                erro += 1
            if erro >= len(palavra):
                erroG += 1
            else:
                pass
            if erroG == 1:
                print(macacoBraco2)
                print(''.join(lp))
            elif erroG == 2:
                print(macacoHead)
                print(''.join(lp))
            elif erroG == 3:
                print(macacoBraco1)
                print(''.join(lp))
            elif erroG == 4:
                print(macacoCorpo)
                print(''.join(lp))
            elif erroG == 5:
                print(macacoPerna2)
                print(''.join(lp))
            elif erroG == 6:
                print(macacoPerna1)
                print(''.join(lp))
            elif erroG == 7:
                print(macacoInteiro)
                print(''.join(lp))
                errou()

if __name__ == "__main__":
    main()