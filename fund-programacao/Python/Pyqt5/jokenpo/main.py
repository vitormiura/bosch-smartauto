import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import centralofGames as mn
import jokenpo as jp

class Menu(mn.Ui_MainWindow):
    def __init__(self, menu_principal):
        self.setupUi(menu_principal)
        self.btnHangman_2.clicked.connect(self.chamar_jokenpo)
        
    def chamar_jokenpo(self):
        self.game = QtWidgets.QWidget()
        self.j = Jokenpo(self.game)
        self.game.show()

class Jokenpo(jp.Ui_Form):
    
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha = ''
    
    def __init__(self, joken_po):
        self.setupUi(joken_po)
        self.btn_pedra.clicked.connect(self.pedra_click)
        self.btn_papel.clicked.connect(self.papel_click)
        self.btn_tesoura.clicked.connect(self.tesoura_click)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_pedra_2.clicked.connect(self.username_input)
        __class__.__sortear()
        
    def username_input(self):
        username = self.lineEdit.text()
        text = 'BEM VINDO, ' + str(username)
        self.titulo.setGeometry(QtCore.QRect(10,30,500,60))
        self.titulo.setText(text)
        self.btn_pedra_2.setEnabled(False)
    
    def verificar_vitoria(self):
        if self.escolha == 'pedra' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("Computador venceu!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'papel':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'papel' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("Computador venceu!")
        elif self.escolha == 'papel' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'pedra' and Jokenpo.escolha == 'papel':
            self.resposta.setText("Computador venceu!")    
            
        elif self.escolha == 'papel' and Jokenpo.escolha == 'papel':
            self.resposta.setText("EMPATE!")
        elif self.escolha == 'pedra' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("EMPATE!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("EMPATE!")
        
        self.btn_pedra.setEnabled(False)
        self.btn_papel.setEnabled(False)
        self.btn_tesoura.setEnabled(False)
    
    def pedra_click(self):
        self.escolha = 'pedra'
        self.verificar_vitoria()
        
    def papel_click(self):
        self.escolha = 'papel'
        self.verificar_vitoria()
        
    def tesoura_click(self):
        self.escolha = 'tesoura'
        self.verificar_vitoria()
    
    def reset(self):
        self.btn_pedra.setEnabled(True)
        self.btn_papel.setEnabled(True)
        self.btn_tesoura.setEnabled(True)
        __class__.__sortear()
        self.resposta.setText("Jogue novamente...")
        
    @staticmethod
    def __sortear():
        __class__.escolha = random.choice(Jokenpo.escolhas)
        print(Jokenpo.escolha)   


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu_principal = QtWidgets.QMainWindow()
    m = Menu(menu_principal)
    menu_principal.show()
    sys.exit(app.exec_())