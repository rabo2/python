import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import random


form_class = uic.loadUiType("mygui08.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        self.arr = ["가위", "바위", "보"]
        self.pb.clicked.connect(self.pbClicked)
        self.le_Mine.returnPressed.connect(self.myenter)
        
    def pbClicked(self):
        self.game()
    def myenter(self):
        self.game()

    def game(self):
        mine = self.le_Mine.text()
        com = self.arr[random.randint(0, 2)]
        result = ""
        
        if mine == com : 
            result = "비김"
            
        elif ((mine == "가위" and com == "보") or (mine == "바위" and com == "가위") or (mine == "보" and com == "바위")) : 
                result = "승리"
        
        else: 
            result = "패배"
        
        self.le_Com.setText(com)
        self.le_Result.setText(result)
 
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()