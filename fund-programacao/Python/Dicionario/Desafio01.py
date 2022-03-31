anos = {}

tot = int(input("Quantidade de anos que deseja adicionar: "))

for i in range(0,tot):
    indice = int(input("Indice: "))
    ano = int(input("Ano: "))
    anos[indice] = ano 
print("Anos salvos:", anos)

def veri(anos):
    bi = int(input("Digite o ano que vc deseja verificar: "))
    for ind in anos.values():
        if ind == bi:
            print('O ano está no dicionario')
            if bi % 400 == 0 and bi % 100 == 0:
                    print(f"{bi} é um ano bissexto")
            elif bi % 4 == 0 and bi % 100 != 0: 
                    print(f"{bi} é bissexto.")
            else:
                    print(f'{bi} não é bissexto.') 
        else:
            pass
veri(anos)


