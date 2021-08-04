import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QMessageBox


form_class = uic.loadUiType("mygui09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("my form")
        self.pb1.clicked.connect(self.pbClicked)
        self.pb2.clicked.connect(self.pbClicked)
        self.pb3.clicked.connect(self.pbClicked)
        self.pb4.clicked.connect(self.pbClicked)
        self.pb5.clicked.connect(self.pbClicked)
        self.pb6.clicked.connect(self.pbClicked)
        self.pb7.clicked.connect(self.pbClicked)
        self.pb8.clicked.connect(self.pbClicked)
        self.pb9.clicked.connect(self.pbClicked)
        self.pb0.clicked.connect(self.pbClicked)
        self.pbCall.clicked.connect(self.pbClickedCall)
        
        
    def pbClicked(self):
        num = self.sender().text()
        str = self.le.text()+num
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