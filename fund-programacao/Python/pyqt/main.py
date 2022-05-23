from PyQt5 import QtWidgets, uic 
import sys
from telas import velha

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('telas/main.ui', self)
        
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.button.clicked.connect(self.printButtonPressed)
        

        self.show()
        
    def printButtonPressed(self):
        print('butao')
        velha = velha.velha_class()
        

app = QtWidgets.QApplication(sys.argv)

window = Ui()

app.exec()
