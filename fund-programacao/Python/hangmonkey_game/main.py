import random
import time
import sys
from macacos import *

def printar_mococo(vida):
    if vida == 7:
        time.sleep(0.5)
        print(macaco1)
    elif vida == 6:
        time.sleep(0.5)
        print(macaco2)
    elif vida == 5:
        time.sleep(0.5)
        print(macaco3)
    elif vida == 4:
        time.sleep(0.5)
        print(macaco4)
    elif vida == 3:
        time.sleep(0.5)
        print(macaco5)
    elif vida == 2:
        time.sleep(0.5)
        print(macaco6)
        print(f"MAIS UM ERRO E O MACACO FALECE!!!")
    elif vida == 1:
        time.sleep(0.5)
        print(macaco7)
        time.sleep(0.5)
        lose()

def main():

    print('Jogo da Forca!')
    time.sleep(0.5)
    op = input('Deseja Iniciar? (S/N) ').lower()
    print("-" * 50)

    if op == 's':
        game()
    else:
        sys.exit()

def win():
    print("-" * 50)
    op = input("GANHASTE! queres jugar dnv?(s/n) ").lower()
    print("-" * 50)
    if op == 's':
        main()
    elif op == 'n':
        exit()
    else:
        print('Opção inválida!')
        win()
        
def lose():
    print("-" * 50)
    op = input("perdeste!, queres jugar dnv?(s/n) ").lower()
    print("-" * 50)
    if op == 's':
        main()
    elif op == 'n':
        exit()

    else:
        print("Opção inválida!")
        lose()

def game():

    print('Sorteando a palavra...')
    print("-" * 50)

    f = open("palavras.txt", "r").read()
    separe = f.replace('\n', '').split(";")   
    sort = separe[random.randint(0, len(separe)-1)]  
    word = sort.split(":") #SORTEIO DA PALAVRA!
    tam = len(word[0])

    print(f'A palavra sorteada tem {tam} letras')
    print(f'Dica -> {word[1]}')
    print("-" * 50)

    dig = []
    chance = 7

    while True:
        temp = ''  
        letra = str(input("Chute uma letra: "))
        dig.append(letra)
        
        for i in word[0]:
            if i in dig:
                temp += i
            else:
                temp += '_'
        
        if temp == word[0]:
            win()
        elif letra == word[0]:
            win()
        else:
            print(temp)
            
        if letra not in word[0]:
            chance -= 1
            printar_mococo(chance)
            
if __name__ == "__main__":
    main()