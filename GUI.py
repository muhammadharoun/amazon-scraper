
import sys
from time import sleep
from PyQt5.QtWidgets import QMainWindow ,QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import QRunnable
# import from PyQt5.QtCore import QRunnable
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from threading import *
import os 


class App(QMainWindow,QRunnable):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(f'{os.getcwd()}/logo.jpg'))
        self.title = 'Amazon scraper'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 420
        self.initUI()
    
    def textBox(self,width,height,x,y,placeholder):
        self.textbox = QLineEdit(self)
        self.textbox.move(x, y)
        self.textbox.resize(width,height)
        self.textbox.setPlaceholderText(placeholder)
        return self.textbox

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  
        self.min_price = self.textBox(170,40,20,20,'min price')
        self.max_price = self.textBox(170,40,200,20,'max price')

        self.min_review = self.textBox(170,40,20,80,'min review')
        self.max_review = self.textBox(170,40,200,80,'max review')

        self.min_rate = self.textBox(170,40,20,140,'min rate')
        self.amazon_link = self.textBox(170,40,200,140,'amazon link')

        self.amazon_link = self.textBox(170,40,200,140,'amazon link')

        self.start_pages = self.textBox(170,40,20,200,'start pages')
        self.end_pages = self.textBox(170,40,200,200,'end pages')
        self.file_name = self.textBox(350,40,20,260,'file name')

        self.keywords = self.textBox(350,40,20,320,'keywords')

        # Create a buttons in the window
        self.button = QPushButton('scrap Data', self)
        self.button.move(20,380)
        self.button2 = QPushButton('update stock', self)
        self.button2.move(120,380)
        self.button.clicked.connect(self.thread1)
        self.button2.clicked.connect(self.thread2)
        self.show()

    def thread1(self):
        t1=Thread(target=self.Operation1)
        t1.start()

    def Operation1(self):    
        print("time start")
        textboxValue = self.textbox1.text()
        print(textboxValue)
        print('textboxValue1')
        sleep(10)
        print("time stop")
  

    def thread2(self):
        t1=Thread(target=self.Operation2)
        t1.start()
  
    def Operation2(self):    
        print("time start")
        textboxValue = self.textbox1.text()
        print(textboxValue)
        print('textboxValue2')
        sleep(10)
        print("time stop")
  





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
