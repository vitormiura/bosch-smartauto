def encontrar_letra():
    palavra = input("Digite a palavra: ")
    lista = list(palavra)
    
  ##  ind = []
    
    letra = input("Digite a letra : ")
    
    for i in range(len(lista)):
        if lista[i] == letra:
          ##  ind.append(i)
            
            print(f'A letra {letra} esta no indice {i+1}')
                
    print(lista)
    ##print(ind)
encontrar_letra ()