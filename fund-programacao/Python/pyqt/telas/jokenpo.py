from PyQt5 import QtCore, QtGui, QtWidgets
import random, sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 530)
        Form.setMinimumSize(QtCore.QSize(450, 530))
        Form.setMaximumSize(QtCore.QSize(450, 530))
        Form.setStyleSheet("background-color:rgb(134, 186, 255);")
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(140, 30, 201, 61))
        self.titulo.setStyleSheet("font: 75 19pt \"MS Shell Dlg 2\";\n"
        "text-decoration: underline;\n"
        "")
        self.titulo.setObjectName("titulo")
        self.btn_pedra = QtWidgets.QPushButton(Form)
        self.btn_pedra.setGeometry(QtCore.QRect(50, 170, 101, 71))
        self.btn_pedra.setStyleSheet("background-color:rgb(127, 127, 127);")
        self.btn_pedra.setObjectName("btn_pedra")
        self.btn_papel = QtWidgets.QPushButton(Form)
        self.btn_papel.setGeometry(QtCore.QRect(170, 170, 101, 71))
        self.btn_papel.setStyleSheet("background-color:rgb(214, 214, 214);")
        self.btn_papel.setObjectName("btn_papel")
        self.btn_tesoura = QtWidgets.QPushButton(Form)
        self.btn_tesoura.setGeometry(QtCore.QRect(300, 170, 101, 71))
        self.btn_tesoura.setStyleSheet("background-color:rgb(200, 87, 67);")
        self.btn_tesoura.setObjectName("btn_tesoura")
        self.resposta = QtWidgets.QLabel(Form)
        self.resposta.setGeometry(QtCore.QRect(60, 280, 331, 111))
        self.resposta.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.resposta.setText("")
        self.resposta.setObjectName("resposta")
        self.btn_reset = QtWidgets.QPushButton(Form)
        self.btn_reset.setGeometry(QtCore.QRect(160, 420, 111, 61))
        self.btn_reset.setStyleSheet("background-color:rgb(143, 150, 158);")
        self.btn_reset.setObjectName("btn_reset")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_pedra_2 = QtWidgets.QPushButton(Form)
        self.btn_pedra_2.setGeometry(QtCore.QRect(330, 120, 71, 31))
        self.btn_pedra_2.setStyleSheet("background-color:rgb(127, 127, 127);")
        self.btn_pedra_2.setAutoDefault(True)
        self.btn_pedra_2.setDefault(True)
        self.btn_pedra_2.setObjectName("btn_pedra_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titulo.setText(_translate("Form", "Jogo Joken Po!"))
        self.btn_pedra.setText(_translate("Form", "Pedra"))
        self.btn_papel.setText(_translate("Form", "Papel"))
        self.btn_tesoura.setText(_translate("Form", "Tesoura"))
        self.btn_reset.setText(_translate("Form", "Resetar"))
        self.btn_pedra_2.setText(_translate("Form", "Enter"))

class Jokenpo(Ui_Form):
    
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
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
