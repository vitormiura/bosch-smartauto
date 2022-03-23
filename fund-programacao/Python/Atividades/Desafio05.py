def main():
    num = input('Escreva os numeros da lista separados por espaço: ')
    list = num.split()

    for i in range(len(list)):
        list[i] = int(list[i])

    ind = []

    busca = int(input('Digite o numero que deseja buscar: '))

    for i in range(len(list)):
        if list[i] == busca:
            ind.append(i)

            print(f'O numero {busca} esta no indice {i+1}')

    print(list)
main()