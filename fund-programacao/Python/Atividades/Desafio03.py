def armstrong1():
    num = int(input("Digite um numero: "))

    p = len(str(num))
    k = num
    soma = 0

    while k > 0:
        d = k % 10
        soma = soma + (d**p)
        k = k//10
    if num == soma:
        print(f'{num} é um numero de armstrong')
    else:
        print(f'{num} não é um numero de armstrong')
armstrong1()

# def armstrong2():
    
# armstrong2()