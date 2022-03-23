print('-=' * 30)
print('\033[1;92mCONTABILIZADOR DE GASTOS\033[m')
print('-=' * 30)

def calculo(quant_grill_loc, quant_normal_loc, quant_sobremesa_loc):
        print('-=' * 30)
        saldofinal = 1200 - ((quant_grill_loc * 11.4) - (quant_normal_loc * 2.8) - (quant_sobremesa_loc * 4.5))
        print(f'\033[1;92mO seu salario final foi de R${saldofinal}\033[m')

def comidas():
    try:
        while True:
            quant_grill_loc = int(input('\033[1;94mQuantos dias você comeu no grill:\033[m '))
            quant_normal_loc = int(input('\033[1;94mQuantos dias você comeu no cardápio normal:\033[m '))
            quant_sobremesa_loc = int(input('\033[1;94mQuantos dias você comeu sobremesa:\033[m '))
            if 0 < quant_grill_loc > 22 or 0 < quant_normal_loc > 22 or 0 < quant_sobremesa_loc > 22:
                print('\033[1;91mERRO! Um valor informados não condiz com a quantidade de dias uteis.')
                print('Digite os valores novamente!\033[m')
            else:
                break
    except:
        print('\033[1;91mERRO! Valor inválido.\033[m')
        
    calculo(quant_grill_loc, quant_normal_loc, quant_sobremesa_loc)

comidas()

