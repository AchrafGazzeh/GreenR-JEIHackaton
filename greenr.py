# GreenR team participation in JEI Hackaton
# This code includes computer vision based on cv2 and yolov5 
# and Qt code for the dashboard



from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import serial.tools.list_ports
from PyQt5.QtGui import QPixmap
import time
import torch
import cv2
import numpy as np
import serial 
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typedetected = QtWidgets.QLabel(self.centralwidget)
        self.typedetected.setGeometry(QtCore.QRect(40, 270, 241, 221))
        self.typedetected.setStyleSheet("")
        self.typedetected.setText("")
        self.typedetected.setPixmap(QtGui.QPixmap("plastic.png"))
        self.typedetected.setScaledContents(True)
        self.typedetected.setObjectName("typedetected")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 330, 191, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 330, 271, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.name.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.totalpoints = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.totalpoints.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.totalpoints.setObjectName("totalpoints")
        self.verticalLayout_2.addWidget(self.totalpoints)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 280, 191, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("plus1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-3, -10, 1041, 611))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("backround.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.detected = QtWidgets.QLabel(self.centralwidget)
        self.detected.setGeometry(QtCore.QRect(20, 520, 291, 41))
        self.detected.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(200, 8, 69);")
        self.detected.setTextFormat(QtCore.Qt.PlainText)
        self.detected.setScaledContents(True)
        self.detected.setWordWrap(False)
        self.detected.setObjectName("detected")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(230, 20, 601, 141))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("greenr.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.bg.raise_()
        self.typedetected.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label.raise_()
        self.detected.raise_()
        self.logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # PLASTIC

        def plastic():
                self.typedetected.setPixmap(QtGui.QPixmap("paper.png"))
                self.detected.setText("PLASTIC DETECTED")
        #PAPER
        def paper():
                self.typedetected.setPixmap(QtGui.QPixmap("paper.png"))
                self.detected.setText("PAPER DETECTED")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)   


        
       
        self.timer.timeout.connect(self.toggle)
        self.timer.start()
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5x')
        self.model.names[39] = 'Plastic'
        self.model.names[41] = 'Paper'
        self.lst = []
        self.cap = cv2.VideoCapture(0)
        self.cap=cv2.cvCaptu
        self.ser= serial.Serial()
        self.ser.port='COM23'
        self.ser.baudrate=9600
        self.ser.open()
    
    def toggle(self):
        ret, frame = self.cap.read()
    
    # Make detections 
        results = self.model(frame)
    #results.print()
    
    # Showing the box and prediction
        cv2.imshow('YOLO', np.squeeze(results.render()))

        df = results.pandas().xyxy[0]
        for i in df['name']: # name->labels
                print(i)
                if i=="Plastic":
                        self.ser.write(bytes('0','utf-8'  ))
                        self.typedetected.setPixmap(QtGui.QPixmap("plastic.png"))
                        self.detected.setText("PLASTIC DETECTED")
                elif i=="Paper":
                        self.ser.write(bytes('1','utf-8'  ))
                        self.typedetected.setPixmap(QtGui.QPixmap("paper.png"))
                        self.detected.setText("PAPER DETECTED")        
        #a=self.detected.text()
        #print(a)

        

                


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "NAME:"))
        self.label_4.setText(_translate("MainWindow", "Total Points:"))
        self.name.setText(_translate("MainWindow", "Ahmed Marnissi"))
        self.totalpoints.setText(_translate("MainWindow", "69"))
        self.detected.setText(_translate("MainWindow", "PLASTIC DETECTED"))



if __name__ == "__main__":
    import sys
    global state
    state=1
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
