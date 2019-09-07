# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#P
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Signup import Ui_Signup
from Options import Ui_Options
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")


class Ui_Dialog(object):
    def signup(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Signup()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def error(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()


    def login(self):
        username=self.textEdit.text()
        password=self.textEdit_2.text()
        cur=mydb.cursor()
        query="select * from CUSTOMERS where NAME=%s and PASSWORD=%s"
        data=cur.execute(query,(username,password))
        a=cur.fetchall()
        if(len(a)>0):
            username=a[0][4]
            self.window=QtWidgets.QDialog()
            self.ui=Ui_Options(username)
            self.ui.setupUi(self.window)
            self.window.show()    
        else:
            self.error("Warning","Incorrect Username or Password")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(855, 633)
        self.Login_head = QtWidgets.QLabel(Dialog)
        self.Login_head.setGeometry(QtCore.QRect(370, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Login_head.setFont(font)
        self.Login_head.setObjectName("Login_head")
        self.Name = QtWidgets.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(230, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Password = QtWidgets.QLabel(Dialog)
        self.Password.setGeometry(QtCore.QRect(230, 250, 80, 21))
        self.Password.setObjectName("Password")
        self.Login = QtWidgets.QPushButton(Dialog)
        self.Login.setGeometry(QtCore.QRect(290, 340, 106, 30))
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(self.login)
        self.Signup = QtWidgets.QPushButton(Dialog)
        self.Signup.setGeometry(QtCore.QRect(440, 340, 106, 30))
        self.Signup.setObjectName("Signup")
        self.Signup.clicked.connect(self.signup)
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(360, 180, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(360, 250, 151, 31))
        self.textEdit_2.setEchoMode(QLineEdit.Password)
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Page"))
        self.Login_head.setText(_translate("Dialog", "Login"))
        self.Name.setText(_translate("Dialog", "Name"))
        self.Password.setText(_translate("Dialog", "Password"))
        self.Login.setText(_translate("Dialog", "Login"))
        self.Signup.setText(_translate("Dialog", "Signup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())













#def Register(self):

        #aid=random.randint(10,10000)
        #mycursor=mydb.cursor()
        #name=self.Nametext.toPlainText()
        #password=self.Passwordtext.toPlainText()
        #city=self.Citytext.toPlainText()
        #state=self.Statetext.toPlainText()
        #Balance=self.Balancetext.toPlainText()
        #sql="insert into CUSTOMERS values(%s,%s,%s,%s,%s)"
        #sql1="insert into ACCOUNT values(%s,%s)"
        #val=(name,password,city,state,aid)
        #val1=(aid,Balance)
        #mycursor.execute(sql,val)
        #mycursor.execute(sql1,val1)
        #mydb.commit()
        

#import mysql.connector
#import random
#mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")
