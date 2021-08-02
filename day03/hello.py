import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbClicked)
    
    def pbClicked(self):
        str = "Good night"
        
        self.lbl.setText(str)
    
        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()