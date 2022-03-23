from os import system
import random
from cores import *

vida = 49
tent = 5

print('--- Jogo da adivinhação ---')

numsort = random.randrange(0, 101)

for i in range(5):          
    tent -= 1
    chute = int(input('Digite um numero de 0 a 100: '))
    
    if chute > 100 or chute < 0:
        print(f"{cores['vermelho']}{bg['branco']}{fx['negrito']} ----- ACERTOU ----- {limpar}")
        chute = int(input('Digite um numero de 0 a 100: '))
    if chute == numsort:
        print(f"{cores['verde']}{bg['branco']}{fx['negrito']} ----- ACERTOU ----- {limpar}")
        break
    else:
        if chute > numsort:
            vida -= (chute - numsort)
        else:
            vida -= (numsort - chute)
    if vida <= 0:
        print(f"{cores['vermelho']}{bg['preto']} Acabou sua vida amigo o numero sorteado era {numsort} {limpar}")
        break
    else: 
        print(f"{cores['preto']}{bg['branco']} --- Tente novamente --- {limpar}")
        print(f"{cores['preto']}{bg['branco']} Você ainda possui {vida} de vida e {tent} tentativas. {limpar}")
