from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket
import os
import sys
import struct
from imgsr import recieve_img
from imgsr import send_img
class DumbDialog(QWidget):
    def __init__(self,  parent = None):
        super(DumbDialog,  self).__init__(parent)
        self._title = "image_loader"
        self._diawidth = 300
        self._diaheight = 450
        self.setWindowTitle(self._title)
        self.setMinimumHeight(self._diaheight)
        self.setMinimumWidth(self._diawidth)
        self.imageView = QLabel("add a image file")
        self.imageView.setAlignment(Qt.AlignCenter)
        self.btn_open = QPushButton("open")
        self.btn_connect=  QPushButton("connect")
        self.btn_connect.clicked.connect(self.on_btn_connect_clicked)
        self.btn_open.clicked.connect(self.on_btn_open_clicked)
        #self.adr_input=QLineEdit('please input the ip you want to connect:')
        self.adr_input=QLineEdit('127.0.0.1')
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.adr_input)
        self.vlayout.addWidget(self.btn_connect)
        self.vlayout.addWidget(self.imageView)
        self.vlayout.addWidget(self.btn_open)
        self.setLayout(self.vlayout)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    @pyqtSlot(bool)
    def on_btn_connect_clicked(self, checked):
        try:
            
            connect_addr=self.adr_input.text()
            self.s.connect((connect_addr, 6666))
        except socket.error as msg:
            print msg
            sys.exit(1)
    
        print self.s.recv(1024)    
    @pyqtSlot(bool)
    def on_btn_open_clicked(self, checked):
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", 
            "Image Files(*.jpg *.jpeg *.png)")[0]
        if len(self.filename):
            '''self.image = QImage(self.filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())
            print self.filename'''
            sendfilepath=str(self.filename)
            send_img(self.s, sendfilepath)
            new_filename=recieve_img(self.s)
            self.image = QImage(new_filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image)) 
            self.resize(self.image.width(), self.image.height())
            
