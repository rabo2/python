import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType("mygui05.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        
        self.pb.clicked.connect(self.pbClicked)
    
    def pbClicked(self):
        num1 = int(self.leA.text())
        num2 = int(self.leB.text())
        num3 = int(self.leC.text())
        result = 0
        
        for i in range(num1,num2+1):
            if i%num3 == 0 :
                result += i
        
        self.leD.setText(str(result))
    
    
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()