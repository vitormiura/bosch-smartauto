from os import system
import random
import time
import sys
from macacos import *

def printar_mococo(vida):
    if vida == 7:
        print(macaco1)
    elif vida == 6:
        print(macaco2)
    elif vida == 5:
        print(macaco3)
    elif vida == 4:
        print(macaco4)
    elif vida == 3:
        print(macaco5)
    elif vida == 2:
        print(macaco6)
    elif vida == 1:
        time.sleep(0.5)
        print(macaco7)
        time.sleep(0.5)
        lose()

def main():
    system('cls')
    print('--------- Jogo da Forca! ----------')
    print('[1] - JOGAR')
    print('[2] - ADICIONAR PALAVRA E DICA')
    print('[3] - REMOVER PALAVRA E DICA')
    print('[4] - SAIR')
    print('-----------------------------------')
    op = input('Escolha a opcao desejada: ')
    print("-" * 50)

    if op == '1':
        game()
    elif op == '2':
        add()
    elif op == '3':
        remove()
    elif op == '4':
        sys.exit()
    else:
        print('Opcao invalida!')
        main()

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

def add():
    with open('palavras.txt', 'a', encoding='utf-8') as p:
        print("ADICIONAR PALAVRA FORCA")
        print("-" * 50)
        while True:
            palavra = input("Digite a palavra a ser adicionada: ").lower()
            dica = input(f"Digite a dica da palavra '{palavra}': ").lower()
            p.write("\n"+palavra+":"+dica+";")
            p.close()
            print('PALAVRA ADICIONADA COM SUCESSO!')
            time.sleep(3)
            main()

def remove():
    f = open("palavras.txt", "r").read() 
    palavras = f.replace('\n', '').split(";")
    print('REMOVER PALAVRA E DICA FORCA!')
    print("-" * 50)
    while True:
        word = input("Digite a palavra a ser removida: ").lower().strip()
        dica = input("Digite a dica da palavra: ").lower().strip()
        linha = (word+":"+dica)
        if linha in palavras:
            index = palavras.index(linha)
            palavras.pop(index)

            temp = ''
            for txt in palavras:
                temp += (txt+';'+'\n')
            with open("palavras.txt", "w", encoding='utf-8') as f:
                f.write(temp)

            print("PALAVRA DELETADA COM SUCESSO!")
            time.sleep(3)
            main()
        else:
            print(f"PALAVRA NAO ENCONTRADA")
            time.sleep(3)
            main()

def game():

    print('Sorteando a palavra...')
    print("-" * 50)

    f = open("palavras.txt", "r").read() 
    separe = f.replace('\n', '').split(";")   
    sort = separe[random.randint(0, len(separe)-1)] #SORTEIO DA PALAVRA! 
    word = sort.split(":") 
    tam = len(word[0])

    print(f'A palavra sorteada tem {tam} letras')
    print(f'Dica -> {word[1]}')
    print("-" * 50)

    dig = []
    chance = 8

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