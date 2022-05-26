from jogodavelha import *

class JogoDaVelha(Ui_MainWindow):
    contador = 1
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.btn2.clicked.connect(self.contar)
        MainWindow.show()
        sys.exit(app.exec_())

    def contar(self):
        print(__class__.contador)
        __class__.contador+=1

if __name__ == "__main__":
    j = JogoDaVelha()