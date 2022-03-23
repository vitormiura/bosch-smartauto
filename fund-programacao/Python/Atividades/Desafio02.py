from os import system
import random

num = 0
ponto_n = 0
ponto_nC = 0
saldo = 18.00
cont = ''
rev = ''

print('----- Jogo dos dados -----')
while saldo > 0:
    print('saldo atual: R$ 18.00')
    while cont != "S":
        num = int(input("Escolha um numero de 1 a 6: "))
        if num < 1 or num > 6:
            while num < 1 or num > 6:
                num = int(input("Numero invalido! Apenas aqueles entre 1 a 6: "))
        nC = random.randrange(1, 7)
        if nC == num:
            while nC == num:
                nC = random.randrange(1, 7)
        print(f"O número que escolhi foi: {nC}")
        sorteado = random.randrange(1, 7) 
        while sorteado != num and sorteado != nC:
            sorteado = random.randrange(1, 7)
            if sorteado == num or sorteado == nC:
                break
        print(f'O numero sorteado pelo Robo foi {sorteado}')
        if sorteado == num:
            ponto_n += 1
            print('E vc Acertou.\n')
        elif sorteado == nC:
            ponto_nC += 1
            print('E vc Errou!.')
        if ponto_nC == 2:
            cont = input("Deseja jogar novamente (S/N): ").lower()
            if rev in "s":
                    break
        elif ponto_n == 2:
            print('Venceu! Revanche?')
            print('SE perder não perderá saldo!')
            print('Se vencer 10 serão acrescentados ao seu saldo!')
            print('Caso não aceite a revanche, ganhará 10 reais.')
            rev = input('Aceita (S/N)? ').lower()
            if rev in "Ss":
                ponto_n = 0
                ponto_nC = 0
                continue
            if rev in "Nn":
                saldo - 7.50
            break
        
