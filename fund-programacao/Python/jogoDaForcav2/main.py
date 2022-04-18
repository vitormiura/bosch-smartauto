import random
import time
import sys
from macacos import *

def printar_boneco(vidas):
    if vidas == 7:
        print(macacoBraco2)
    elif vidas == 6:
        print(macacoHead)
    elif vidas == 5:
        print(macacoBraco1)
    elif vidas == 4:
        print(macacoCorpo)
    elif vidas == 3:
        print(macacoPerna2)
    elif vidas == 2:
        print(macacoPerna1)
    elif vidas == 1:
        print(macacoInteiro)
        print(f"MAIS UM ERRO E O MACACO CAI!!!")

def main():

    print('Jogo da Forca!')
    time.sleep(0.5)
    op = input('Deseja Iniciar? (S/N)').lower()

    if op == 's':
        game()
    else:
        sys.exit()

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
    sort = row_arr[random.randint(0, len(row_arr)-1)]  
    pala = sort.split(":")

    tam = len(pala[0])
    ind = pala.index(pala[0])


    print(f'A palavra sorteada tem {tam} letras')

    print(f'Dica -> {pala[1]}')

    dig = []


    while True:
        chance = 7
        temp = ''
                
        letra = str(input("Chute uma letra: "))
        if len(letra) > 1:
            print('Uma letra por vez!')
            continue
        
        dig.append(letra)
        
        for i in pala[0]:
            if i in dig:
                temp += i
            else:
                temp += '_'
        
        if temp == pala[0]:
            print('Vc venceu!')
        else:
            print(temp)
            
        if letra not in pala[0]:
            chance -+ 1
            
        print(printar_boneco(chance))
            

if __name__ == "__main__":
    main()