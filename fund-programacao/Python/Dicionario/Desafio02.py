dic = {'joao' : 1231-5151, 'pedro' : 1231-5151, 'carl' : 1231-5151, 'jujjj' : 1231-5151, 'ahaha' : 1231-5151, 'joawd' : 1231-5151, 'joaodawd' : 1231-5151, 'dadjoao' : 1231-5135, 'jodaao' : 1231-5151, 'awdjoao' : 1231-5151}

print(dic)

def let(dic):   
    aaa = str(input('Digite a primeira letra que vc deseja verificar'))

    for ind in dic.keys():
        if ind[0] == aaa.lower():
            print("\n%s: %s" %(ind, dic[ind]))
        else:
            pass
let(dic)