from PyQt5 import QtCore, QtGui, QtWidgets
import random
import smtplib
import csv

class Ui_passforget(object):
    def setupUi(self, passforget):
        passforget.setObjectName("passforget")
        passforget.resize(619, 322)
        passforget.setMinimumSize(QtCore.QSize(619, 322))
        passforget.setMaximumSize(QtCore.QSize(619, 322))
        self.label = QtWidgets.QLabel(passforget)
        self.label.setGeometry(QtCore.QRect(370, 60, 31, 31))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(passforget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 201, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(passforget)
        self.pushButton.setGeometry(QtCore.QRect(210, 110, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(passforget)
        self.label_2.setGeometry(QtCore.QRect(0, 140, 611, 20))
        self.label_2.setObjectName("label_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(passforget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 180, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_3 = QtWidgets.QLabel(passforget)
        self.label_3.setGeometry(QtCore.QRect(320, 160, 171, 16))
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(passforget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(passforget)
        QtCore.QMetaObject.connectSlotsByName(passforget)

    def change(self):
        with open('userdetails.csv', 'r') as csvfile:
             pcsv = csv.reader(csvfile)
             for row in pcsv:
                 if (row[3]== self.eemail):
                     print ("Password : " + row[4])
                     


    def sendval(self):
        self.email = self.lineEdit.text()
        with open('userdetails.csv', 'r') as csvfile:
             pcsv = csv.reader(csvfile)
             for row in pcsv:
                 if (row[3] == self.email):
                     print("code send")
                     self.eemail = self.email
                     self.sendmail()       
                 else:
                     print("wrong mail")

    def sendmail(self):
        self.seccode = random.randint(100000,999999)
        sec = str(self.seccode)
        user = "your email"
        password = "email password"
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  #senf email by smtp
        server.ehlo()
        server.login(user, password)
        to = str(self.email)
        server.sendmail(user, to , "Code : " + sec)

    def checkcode(self):
        self.checks = int(self.lineEdit_3.text())
        if (self.checks != self.seccode):
            self.lineEdit_2.setText("Code not mach")
        else : 
            self.lineEdit_2.setText("mach")
            self.change()

    def retranslateUi(self, passforget):
        _translate = QtCore.QCoreApplication.translate
        passforget.setWindowTitle(_translate("passforget", "Forget Password"))
        self.label.setText(_translate("passforget", "ایمیل"))
        self.pushButton.setText(_translate("passforget", "ارسال کد"))
        self.label_2.setText(_translate("passforget", "-----------------------------------------------------------------------------------------------------------------------------------------"))
        self.label_3.setText(_translate("passforget", "کد دریافتی از ایمل را وارد کنید"))
        self.pushButton_2.setText(_translate("passforget", "تایید"))
        self.pushButton.clicked.connect(lambda : self.sendval() )
        self.pushButton_2.clicked.connect(lambda : self.checkcode() )


