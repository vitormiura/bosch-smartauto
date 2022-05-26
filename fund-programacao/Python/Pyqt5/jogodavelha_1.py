from PyQt5 import uic, QtWidgets
import sys

def jogador_x():
    print("X")
    jogo.btn1.setText("X")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    jogo:QtWidgets.QMainWindow = uic.loadUi("jogodavelha.ui")
    jogo.btn1.clicked.connect(jogador_x)
    #jogo.btn1:QtWidgets.QPushButton
    #jogo.btn1.clicked()
    jogo.show()
    sys.exit(app.exec_())