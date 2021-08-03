import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import random


form_class = uic.loadUiType("mygui06.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        
        self.pb.clicked.connect(self.pbClicked)
        self.leA.returnPressed.connect(self.myenter)
        
    def myenter(self):
        self.gameStart()

    def pbClicked(self):
        self.gameStart()
        

    def gameStart(self):
        mine = self.leA.text()
        com = random.randrange(1, 7)
        result = ""
        if (mine == "홀" and com % 2 != 0) or (mine == "짝" and com % 2 == 0):
            result = "승리"
        else:
            result = "패배"
        self.leB.setText(str(com))
        self.leC.setText(result)
        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()