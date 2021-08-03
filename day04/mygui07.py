import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("mygui07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        
        self.pb.clicked.connect(self.pbClicked)
        self.le.returnPressed.connect(self.myenter)
        
    def pbClicked(self):
        self.gugudan()
    
    def myenter(self):
        self.gugudan()

    def gugudan(self):
        inputNum = self.le.text()
        multipel = ""
        for i in range(1, 10):
            multipel += "{} * {} = {}\n".format(inputNum, i, int(inputNum)*i)
            
        self.te.setText(multipel)

 
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()