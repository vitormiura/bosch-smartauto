from os import system


class Tv:

    def __init__(self, m):
        self.modelo = m
        self.on = False
        self.canal = ''
        self.vol = 50

    def get_mod(self):
        return self.modelo

    def set_canalbaixo(self):
        self.canal -= 1

    def set_canalcima(self):
        self.canal += 1

if __name__ == '__main__':
    tv = Tv('xiaomi')
      
    op = input('Deseja Ligar (S/N): ').lower()
    
    if op == 's':
        tv.on = True  
    else:
        system.exit()
                  
    tv.canal = int('Canal desejado: ')
    
    print('Ligada:', tv.on)
    print('Canal inicial:', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal -', tv.canal)