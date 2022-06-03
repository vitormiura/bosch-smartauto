from PyQt5 import QtWidgets, uic 
import sys
from telas import velha as vl
from telas import menu as mn
from telas import jokenpo as jk

class Menu(mn.Ui_MainWindow):
    def __init__(self, menu_principal):
        self.setupUi(menu_principal)
        self.velhaButton.clicked.connect(self.openVelha)
        self.jokenpoButton.clicked.connect(self.openJokenpo)
        #self.forcaButton.clicked.connect(self.openVelha)
        
    def openVelha(self):
        self.game = QtWidgets.QMainWindow()
        self.j = vl.velhinha(self.game)
        self.game.show()
    
    def openForca(self):
        pass
    
    def openJokenpo(self):
        self.game = QtWidgets.QWidget()
        self.j = jk.Jokenpo(self.game)
        self.game.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu_principal = QtWidgets.QMainWindow()
    m = Menu(menu_principal)
    menu_principal.show()
    sys.exit(app.exec_())
