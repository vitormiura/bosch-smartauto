def main():
    frase = input("Digite a frase para verificar se é um palindromo! ").upper().replace(" ", "")

    if frase == frase[::-1]:
        print("É um palíndromo")
    else:
        print("A frase não é um palíndromo")
main()