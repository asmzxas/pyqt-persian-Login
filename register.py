from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import smtplib 

class Ui_register(object):
    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.setEnabled(True)
        register_2.resize(501, 529)
        register_2.setMinimumSize(QtCore.QSize(501, 529))
        register_2.setMaximumSize(QtCore.QSize(501, 529))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        register_2.setWindowIcon(icon)
        register_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horizontalLayoutWidget = QtWidgets.QWidget(register_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 390, 195, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(register_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 40, 191, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.lastname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lastname.setObjectName("lastname")
        self.verticalLayout.addWidget(self.lastname)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.repassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassword.setObjectName("repassword")
        self.verticalLayout.addWidget(self.repassword)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(register_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 40, 81, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_12.setFrame(False)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(register_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 40, 101, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def signup(self):
       i = 1
       self.name1 = self.name.text()
       if (self.name1 != ''):
           i = i + 1
       #+++++++++++++++++++++++++++++++++++++++++++++
       self.lastname1 = self.lastname.text() 
       if (self.lastname1 != ''):
           i = i + 1
        #++++++++++++++++++++++++++++++++++++++++++++ 
       self.username1 = self.username.text() 
       if (self.username1 != ''):
           i = i + 1 
        #++++++++++++++++++++++++++++++++++++++++++++ 
       self.email1 = self.email.text()
       if (self.email1 != ''):
           i = i + 1 
        #++++++++++++++++++++++++++++++++++++++++++++ 
       self.password1 = self.password.text()
       if (self.password1 != ''):
           i = i + 1 
        #++++++++++++++++++++++++++++++++++++++++++++  
       self.repassword1 = self.repassword.text()
       rn = str(self.repassword1) 
       n = str(self.password1)
       if (rn != n):
           i = i + 1
       if ( i == 6):
           if (rn == n):
               with open('userdetails.csv', 'a') as save:
                   save.write(self.name1 + ',' + self.lastname1 + ',' + self.username1 + ',' + self.email1 + ',' + self.password1 +"\n")
                   self.send_simple_message()
                   self.delete()
           else:
               print("wrong")
               self.repassword.setText('')
       else:
           print("fill all the blanks")

    def send_simple_message(self):
        user = "your email"
        password = "email password"
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  #senf email by smtp
        server.ehlo()
        server.login(user, password)
        to = str(self.email1)
        server.sendmail(user, to , "Registerd successfully " + to + " - " + self.name1 + " " + self.lastname1)

    def delete(self):
        self.name.setText('')
        self.lastname.setText('') 
        self.username.setText('') 
        self.email.setText('')
        self.password.setText('')    
        self.repassword.setText('')    

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Register Form"))
        self.pushButton_2.setText(_translate("register_2", "ثبت نام"))
        self.pushButton.setText(_translate("register_2", "پاک کردن"))
        self.lineEdit_7.setText(_translate("register_2", "نام"))
        self.lineEdit_8.setText(_translate("register_2", "نام خانوادگی"))
        self.lineEdit_9.setText(_translate("register_2", "نام کاربری"))
        self.lineEdit_10.setText(_translate("register_2", "ایمیل"))
        self.lineEdit_6.setText(_translate("register_2", "رمز عبور"))
        self.lineEdit_12.setText(_translate("register_2", "تکرار رمز عبور"))

