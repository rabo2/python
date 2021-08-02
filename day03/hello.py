import sys
from PyQt5.Qt import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()