import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType("mygui09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        self.pb1.clicked.connect(self.pbClicked1)
        self.pb2.clicked.connect(self.pbClicked2)
        self.pb3.clicked.connect(self.pbClicked3)
        self.pb4.clicked.connect(self.pbClicked4)
        self.pb5.clicked.connect(self.pbClicked5)
        self.pb6.clicked.connect(self.pbClicked6)
        self.pb7.clicked.connect(self.pbClicked7)
        self.pb8.clicked.connect(self.pbClicked8)
        self.pb9.clicked.connect(self.pbClicked9)
        self.pb0.clicked.connect(self.pbClicked0)
        self.pbCall.clicked.connect(self.pbClickedCall)
        
        
    def pbClicked1(self):
        str = self.le.text()+"1"
        self.le.setText(str)
        
        
    def pbClicked2(self):
        str = self.le.text()+"2"
        self.le.setText(str)
        
        
    def pbClicked3(self):
        str = self.le.text()+"3"
        self.le.setText(str)
        
        
    def pbClicked4(self):
        str = self.le.text()+"4"
        self.le.setText(str)
        
        
    def pbClicked5(self):
        str = self.le.text()+"5"
        self.le.setText(str)
        
        
    def pbClicked6(self):
        str = self.le.text()+"6"
        self.le.setText(str)
        
        
    def pbClicked7(self):
        str = self.le.text()+"7"
        self.le.setText(str)
        
        
    def pbClicked8(self):
        str = self.le.text()+"8"
        self.le.setText(str)
        
        
    def pbClicked9(self):
        str = self.le.text()+"9"
        self.le.setText(str)
        
        
    def pbClicked0(self):
        str = self.le.text()+"0"
        self.le.setText(str)
    
    def pbClickedCall(self, event):
        reply = QMessageBox.question(self, 'Message', 'Calling..'+self.le.text(),QMessageBox.No) 

        if reply == QMessageBox.No:
            event.ignore()
        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()