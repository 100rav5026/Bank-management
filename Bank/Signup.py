# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector
import random
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

class Ui_Signup(object):
    def message(self,title,message1):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(str(message1))
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def Register(self):
        aid=random.randint(1,10000)
        self.message("Account ID",aid)
        mycursor=mydb.cursor()
        name=self.Nametext.toPlainText()
        password=self.Passwordtext.text()
        city=self.Citytext.toPlainText()
        state=self.Statetext.toPlainText()
        Balance=self.Balancetext.toPlainText()
        sql="insert into CUSTOMERS values(%s,%s,%s,%s,%s)"
        sql1="insert into ACCOUNT values(%s,%s)"
        val=(name,password,city,state,aid)
        val1=(aid,Balance)
        mycursor.execute(sql,val)
        mycursor.execute(sql1,val1)
        mydb.commit()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 565)
        self.Signup_label = QtWidgets.QLabel(Dialog)
        self.Signup_label.setGeometry(QtCore.QRect(250, 40, 80, 21))
        self.Signup_label.setObjectName("Signup_label")
        self.Name = QtWidgets.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(110, 100, 80, 21))
        self.Name.setObjectName("Name")
        self.Password = QtWidgets.QLabel(Dialog)
        self.Password.setGeometry(QtCore.QRect(100, 160, 80, 21))
        self.Password.setObjectName("Password")
        self.City = QtWidgets.QLabel(Dialog)
        self.City.setGeometry(QtCore.QRect(110, 230, 80, 21))
        self.City.setObjectName("City")
        self.State = QtWidgets.QLabel(Dialog)
        self.State.setGeometry(QtCore.QRect(110, 290, 80, 21))
        self.State.setObjectName("State")
        self.RegisterPush = QtWidgets.QPushButton(Dialog)
        self.RegisterPush.setGeometry(QtCore.QRect(190, 460, 106, 30))
        self.RegisterPush.setObjectName("RegisterPush")
        self.RegisterPush.clicked.connect(self.Register)
        self.Balance = QtWidgets.QLabel(Dialog)
        self.Balance.setGeometry(QtCore.QRect(100, 370, 80, 21))
        self.Balance.setObjectName("Balance")
        self.Nametext = QtWidgets.QTextEdit(Dialog)
        self.Nametext.setGeometry(QtCore.QRect(240, 90, 171, 31))
        self.Nametext.setObjectName("Nametext")
        self.Passwordtext = QtWidgets.QLineEdit(Dialog)
        self.Passwordtext.setGeometry(QtCore.QRect(240, 160, 171, 31))
        self.Passwordtext.setObjectName("Passwordtext")
        self.Passwordtext.setEchoMode(QLineEdit.Password)
        self.Citytext = QtWidgets.QTextEdit(Dialog)
        self.Citytext.setGeometry(QtCore.QRect(240, 220, 171, 31))
        self.Citytext.setObjectName("Citytext")
        self.Statetext = QtWidgets.QTextEdit(Dialog)
        self.Statetext.setGeometry(QtCore.QRect(240, 290, 171, 31))
        self.Statetext.setObjectName("Statetext")
        self.Balancetext = QtWidgets.QTextEdit(Dialog)
        self.Balancetext.setGeometry(QtCore.QRect(240, 370, 171, 31))
        self.Balancetext.setObjectName("Balancetext")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.Signup_label.setText(_translate("Dialog", "Signup"))
        self.Name.setText(_translate("Dialog", "Name"))
        self.Password.setText(_translate("Dialog", "Password"))
        self.City.setText(_translate("Dialog", "City"))
        self.State.setText(_translate("Dialog", "State"))
        self.RegisterPush.setText(_translate("Dialog", "Register"))
        self.Balance.setText(_translate("Dialog", "Balance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

