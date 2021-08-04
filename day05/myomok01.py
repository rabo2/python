import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QIcon, QPushButton, QSize


form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(500,500,400,400)
        self.setWindowTitle("my form")
        self.check = True
        
        for j in range(0,10):
            for i in range(0,10):
                obj = QPushButton(self)
                obj.setGeometry(i*40,j*40,40,40)
                obj.setIcon(QIcon("0.png"))
                obj.setIconSize(QSize(40,40))


if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()