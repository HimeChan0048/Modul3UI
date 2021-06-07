from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import math
from PyQt5.QtCore import QTimer
import random


# ser = serial.Serial('COM4',512000,parity='E',stopbits=1,timeout=3) #when using serial only
ser=serial.Serial() #when not using serial. Switch to the upper mode when using serial

TenStations=[1,5,18,25,36,50,54,60,62,70] #config the stations 
frame2station=0
checksum=0
##################################################################################################################################
#calculation
##################################################################################################################################
cos1=math.cos(math.radians(TenStations[0]*5))
sin1=math.sin(math.radians(TenStations[0]*5))
x1=270-(cos1*200)
y1=250+(sin1*200)
cos2=math.cos(math.radians(TenStations[1]*5))
sin2=math.sin(math.radians(TenStations[1]*5))
x2=270-(cos2*200)
y2=250+(sin2*200)
cos3=math.cos(math.radians(TenStations[2]*5))
sin3=math.sin(math.radians(TenStations[2]*5))
x3=270-(cos3*200)
y3=250+(sin3*200)
cos4=math.cos(math.radians(TenStations[3]*5))
sin4=math.sin(math.radians(TenStations[3]*5))
x4=270-(cos4*200)
y4=250+(sin4*200)
cos5=math.cos(math.radians(TenStations[4]*5))
sin5=math.sin(math.radians(TenStations[4]*5))
x5=270-(cos5*200)
y5=250+(sin5*200)
cos6=math.cos(math.radians(TenStations[5]*5))
sin6=math.sin(math.radians(TenStations[5]*5))
x6=270-(cos6*200)
y6=250+(sin6*200)
cos7=math.cos(math.radians(TenStations[6]*5))
sin7=math.sin(math.radians(TenStations[6]*5))
x7=270-(cos7*200)
y7=250+(sin7*200)
cos8=math.cos(math.radians(TenStations[7]*5))
sin8=math.sin(math.radians(TenStations[7]*5))
x8=270-(cos8*200)
y8=250+(sin8*200)
cos9=math.cos(math.radians(TenStations[8]*5))
sin9=math.sin(math.radians(TenStations[8]*5))
x9=270-(cos9*200)
y9=250+(sin9*200)
cos10=math.cos(math.radians(TenStations[9]*5))
sin10=math.sin(math.radians(TenStations[9]*5))
x10=270-(cos10*200)
y10=250+(sin10*200)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1036, 658)
##################################################################################################################################
#palette
##################################################################################################################################
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 201, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 12, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 10, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 12, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 5, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 2, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 4, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        MainWindow.setPalette(palette)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
##################################################################################################################################
#widgets
##################################################################################################################################
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Status = QtWidgets.QGroupBox(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(490, 20, 451, 561))
        self.Status.setPalette(palette)
        self.Status.setObjectName("Status")
        self.CurrentPos = QtWidgets.QGroupBox(self.Status)
        self.CurrentPos.setGeometry(QtCore.QRect(10, 30, 421, 281))
        self.CurrentPos.setPalette(palette)
        self.CurrentPos.setObjectName("CurrentPos")
        self.Velo = QtWidgets.QLabel(self.CurrentPos)
        self.Velo.setGeometry(QtCore.QRect(30, 20, 241, 41))
        self.Velo.setPalette(palette)
        self.Velo.setObjectName("Velo")
        self.Accel = QtWidgets.QLabel(self.CurrentPos)
        self.Accel.setGeometry(QtCore.QRect(30, 100, 231, 41))
        self.Accel.setPalette(palette)
        self.Accel.setObjectName("Accel")
        self.label_3 = QtWidgets.QLabel(self.CurrentPos)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 251, 21))
        self.label_3.setPalette(palette)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.CurrentPos)
        self.pushButton.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButton.setPalette(palette)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendav)
        self.pushButton_2 = QtWidgets.QPushButton(self.CurrentPos)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.sendaa)
        self.pushButton_3 = QtWidgets.QPushButton(self.CurrentPos)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.pushButton_3.setPalette(palette)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sendsta)
        self.manualaa = QtWidgets.QLineEdit(self.CurrentPos)
        self.manualaa.setValidator(QtGui.QDoubleValidator(0.0, 10.0, 2))
        self.manualaa.setGeometry(QtCore.QRect(100, 150, 111, 21))
        self.manualaa.setText("")
        self.manualaa.setObjectName("manualaa")
        self.manualav = QtWidgets.QLineEdit(self.CurrentPos)
        self.manualav.setValidator(QtGui.QDoubleValidator(0.0, 10.0, 2))
        self.manualav.setGeometry(QtCore.QRect(100, 70, 111, 21))
        self.manualav.setText("")
        self.manualav.setObjectName("manualav")
        self.manualstation = QtWidgets.QLineEdit(self.CurrentPos)
        self.manualstation.setGeometry(QtCore.QRect(100, 230, 111, 21))
        self.manualstation.setText("")
        self.manualstation.setObjectName("manualstation")
        self.Gripper = QtWidgets.QGroupBox(self.Status)
        self.Gripper.setGeometry(QtCore.QRect(10, 320, 421, 151))
        self.Gripper.setPalette(palette)
        self.Gripper.setObjectName("Gripper")
        self.GripperStatus = QtWidgets.QLabel(self.Gripper)
        self.GripperStatus.setGeometry(QtCore.QRect(30, 30, 231, 41))
        self.GripperStatus.setPalette(palette)
        self.GripperStatus.setObjectName("GripperStatus")
        self.label_2 = QtWidgets.QLabel(self.Gripper)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 41))
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.enable = QtWidgets.QPushButton(self.Gripper)
        self.enable.setGeometry(QtCore.QRect(140, 80, 75, 23))
        self.enable.setPalette(palette)
        self.enable.setObjectName("enable")
        self.enable.clicked.connect(self.gron)
        self.disable = QtWidgets.QPushButton(self.Gripper)
        self.disable.setGeometry(QtCore.QRect(230, 80, 75, 23))
        self.disable.setPalette(palette)
        self.disable.setObjectName("disable")
        self.disable.clicked.connect(self.grof)
        self.Connect = QtWidgets.QPushButton(self.Status)
        self.Connect.setGeometry(QtCore.QRect(120, 490, 91, 31))
        self.Connect.setPalette(palette)
        self.Connect.setObjectName("Connect")
        self.Connect.clicked.connect(self.botcon)
        self.Disconnect = QtWidgets.QPushButton(self.Status)
        self.Disconnect.setGeometry(QtCore.QRect(250, 490, 91, 31))
        self.Disconnect.setPalette(palette)
        self.Disconnect.setObjectName("Disconnect")
        self.Disconnect.clicked.connect(self.botdcon)
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(215, 550, 91, 31))
        self.Home.setPalette(palette)
        self.Home.setObjectName("Connect")
        self.Home.clicked.connect(self.gohome)
        self.Gosta = QtWidgets.QPushButton(self.centralwidget)
        self.Gosta.setGeometry(QtCore.QRect(215, 590, 91, 31))
        self.Gosta.setPalette(palette)
        self.Gosta.setObjectName("Connect")
        self.Gosta.clicked.connect(self.gogosta)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 400, 400))
        self.label.setPalette(palette)
        self.label.setText("adsfasdf")
        self.label.setPixmap(QtGui.QPixmap("./dd.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
##################################################################################################################################
#button
##################################################################################################################################
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(y1, x1, 21, 21))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.bb1)

        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(y2, x2, 21, 21))
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.bb2)

        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(y3, x3, 21, 21))
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.bb3)

        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(y4, x4, 21, 21))
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.bb4)

        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(y5, x5, 21, 21))
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.bb5)

        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(y6, x6, 21, 21))
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.bb6)

        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(y7, x7, 21, 21))
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.bb7)

        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(y8, x8, 21, 21))
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.bb8)

        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(y9, x9, 21, 21))
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.bb9)

        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(y10, x10, 21, 21))
        self.b10.setObjectName("b10")
        self.b10.clicked.connect(self.bb10)

        self.b1.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b2.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b3.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b4.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b5.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b6.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b7.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b8.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b9.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
        self.b10.setStyleSheet('border-radius:10px;background-color:white;border-style:outset;border-color:black;border-width:1px')
##################################################################################################################################
#arrow
##################################################################################################################################
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(60,80,400,400))
        self.arrowpng=QtGui.QPixmap("./arrow.png")
        self.arrow.setPixmap(self.arrowpng)
        self.rot=QtGui.QTransform()
        self.rot=0
        self.arrowtrans=QtGui.QTransform().rotate(self.rot)
        self.arrowpng=self.arrowpng.transformed(self.arrowtrans,QtCore.Qt.SmoothTransformation)
        self.arrow.setPixmap(self.arrowpng)
        self.arrow.setAlignment(QtCore.Qt.AlignCenter)

##################################################################################################################################
#what is this
##################################################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##################################################################################################################################
#1sec timer
##################################################################################################################################
        self.first_timer = QTimer()
        self.first_timer.timeout.connect(self.timer_function)
        self.first_timer.start(1000)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Status.setTitle(_translate("MainWindow", "Status"))
        self.CurrentPos.setTitle(_translate("MainWindow", "Position"))
        self.Velo.setText(_translate("MainWindow", "Angular Velocity : 0 rpm"))
        self.Accel.setText(_translate("MainWindow", "Angular Position :"))
        self.label_3.setText(_translate("MainWindow", "Current Station :"))
        self.pushButton.setText(_translate("MainWindow", "Set"))
        self.pushButton_2.setText(_translate("MainWindow", "Set"))
        self.pushButton_3.setText(_translate("MainWindow", "Set"))
        self.Gripper.setTitle(_translate("MainWindow", "Gripper"))
        self.GripperStatus.setText(_translate("MainWindow", "Status :"))
        self.label_2.setText(_translate("MainWindow", "manual control"))
        self.enable.setText(_translate("MainWindow", "Enable"))
        self.disable.setText(_translate("MainWindow", "Disable"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Home.setText(_translate("Mainwindow","Home"))
        self.Gosta.setText(_translate("Mainwindow","Go"))
##################################################################################################################################
#checksum
##################################################################################################################################
    def checksum(self,Data_Frame):
        return ([(~(sum(Data_Frame)%256))%256])

##################################################################################################################################
#buttons
##################################################################################################################################
    def sendav(self):
        if float(self.manualav.text())>10:
            av=10
        else:
            av=self.manualav.text()
        self.Velo.setText("Angular Velocity :" + str(av)+" rpm")
        nocheck=[149,int(av)]
        ser.write([148,int(av),self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
        # print([148,int(av),self.checksum(nocheck)[0]])

    def sendaa(self):
        ap=self.manualaa.text()
        apb=int(ap).to_bytes(2,'big')
        abp1=int.from_bytes(apb[:1],'big')
        abp2=int.from_bytes(apb[-1:],'big')
        self.Accel.setText("Angular Position :" + str(ap))
        nocheck=[149,abp1,abp2]
        ser.write([149,apb[:1],apb[-1:],self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
        # print([149,apb[:1],apb[-1:],self.checksum(nocheck)[0]])

    def sendsta(self):
        mulsta=self.manualstation.text()
        sometemplist=mulsta.split(",")
        print(sometemplist)
        if len(sometemplist)>1:
            nooneknow=[151,len(sometemplist)]
            for whatisthis in sometemplist:
                nooneknow.append(int(whatisthis))
            nooneknow.append(self.checksum(nooneknow)[0])
            ser.write(nooneknow)
            while(ser.readline()!='\x58\x75'):
                pass
            # print(nooneknow)
        elif len(sometemplist)==1:
            nocheck=[150,int(sometemplist[0])]
            ser.write([150,int(sometemplist[0]),self.checksum(nocheck)[0]])
            while(ser.readline()!='\x58\x75'):
                pass
            # print([150,int(sometemplist[0]),self.checksum(nocheck)[0]])

    def gron(self):
        ser.write([156,self.checksum([156])[0]])
        while(ser.readline()!='\x58\x75'):
            pass
        self.GripperStatus.setText("Status : On")
    def grof(self):
        ser.write([157,self.checksum([157])[0]])
        while(ser.readline()!='\x58\x75'):
            pass
        self.GripperStatus.setText("Status : Off")
    def botcon(self):
        ser.write([146,self.checksum([146])[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def botdcon(self):
        ser.write([147,self.checksum([147])[0]])
        while(ser.readline()!='\x58\x75'):
            pass

    def gohome(self):
        ser.write([158,self.checksum([158])[0]])
        while(ser.readline()!='\x58\x75'):
            pass

    def gogosta(self):
        ser.write([152,self.checksum([152])[0]])
        while(ser.readline()!='\x58\x75'):
            pass
        while(ser.readline()!='\x46\x6E'):
            pass
        
        
    def bb1(self):        
        nocheck=[150,1]
        ser.write([150,1,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb2(self):
        nocheck=[150,2]
        ser.write([150,2,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb3(self):
        nocheck=[150,3]
        ser.write([150,3,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb4(self):
        nocheck=[150,4]
        ser.write([150,4,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb5(self):
        nocheck=[150,5]
        ser.write([150,5,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb6(self):
        nocheck=[150,6]
        ser.write([150,6,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb7(self):
        nocheck=[150,7]
        ser.write([150,7,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb8(self):
        nocheck=[150,8]
        ser.write([150,8,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb9(self):
        nocheck=[150,9]
        ser.write([150,9,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass
    def bb10(self):
        nocheck=[150,10]
        ser.write([150,10,self.checksum(nocheck)[0]])
        while(ser.readline()!='\x58\x75'):
            pass

    def timer_function(self):
        print("1sec")

            #uncomment these lines when using serial
        # ser.write([153,self.checksum([153])[0]])
        # while(ser.readline()!='\x58\x75'):
        #     pass
        # currentsta=ser.readline()[1]
        # ser.write("\x58\x75")
        # self.label_3.setText("Current Station : "+str(currentsta))
        # ser.write([154,self.checksum([154])[0]])                
        # while(ser.readline()!='\x58\x75'):
        #     pass
        # currentaa=ser.readline()[1:3]
        # ser.write("\x58\x75")  
        # aaint=int.from_bytes(currentaa,"big")
        # self.Accel.setText("Angular Position :" + str(aaint))
        # self.arrowpng=QtGui.QPixmap("./arrow.png")
        # self.rot=math.degrees(aaint/1000)
        # self.arrowtrans=QtGui.QTransform().rotate(self.rot)
        # self.arrowpng=self.arrowpng.transformed(self.arrowtrans)
        # self.arrow.setPixmap(self.arrowpng)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    torarion=0
    MainWindow.show()
    sys.exit(app.exec_())
