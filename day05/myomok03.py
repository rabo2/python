import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QIcon, QPushButton, QSize


form_class = uic.loadUiType("myomok03.ui")[0]

class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,1,2,1,0, 0,0,0,0,0],
                [0,2,1,2,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                                      
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2d = [
                
            ]
        
        self.setWindowTitle("my form")
        self.flag_wb = True
        
        for i in range(0,10):
            line = []
            for j in range(0,10):
                obj = QPushButton(self)
                obj.setGeometry(j*40,i*40,40,40)
                obj.setIcon(QIcon("0.png"))
                obj.setIconSize(QSize(40,40))
                obj.clicked.connect(self.myChange)
                obj.setToolTip("{},{}".format(str(i), str(j)))
                line.append(obj)
            
            self.pb2d.append(line)
            
        self.myrender()    
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon("0.png"))
        
                elif self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon("1.png"))

                elif self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
                
                    
    def myChange(self):
        self.putStone(self.flag_wb)
            
            
    def putStone(self, flag):
        tool = self.sender().toolTip()
        arr = tool.split(",")
        i = int(arr[0])
        j = int(arr[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        if flag :
            self.arr2d[i][j] = 1
        else : 
            self.arr2d[i][j] = 2
                
                
        self.myrender()
        self.flag_wb = not self.flag_wb
        
        
        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    