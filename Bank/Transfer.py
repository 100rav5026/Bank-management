# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Transfer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

class Ui_Transfer(object):
    def success(self,title,message):
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
    def __init__(self,username):
        self.username=username
    def trans(self):
        mycursor=mydb.cursor()
        rate=int(self.Amount1text.text())
        aidt=self.Accounttext.text()
        username=self.username
        query1="select BALANCE from ACCOUNT where AID=%s"
        mycursor.execute(query1,[aidt])
        x=mycursor.fetchall()
        balance1=int(x[0][0])
        query2="select BALANCE from ACCOUNT where AID=%s"
        mycursor.execute(query2,[username])
        y=mycursor.fetchall()
        balance2=int(y[0][0])
        balance1=int(balance1)+int(rate)
        balance2=int(balance2)-int(rate)
        if rate<balance2 and rate>0:
            query3="Update ACCOUNT SET BALANCE=%s where AID=%s"
            mycursor.execute(query3,[balance2,username])
            query4="Update ACCOUNT SET BALANCE=%s where AID=%s"
            mycursor.execute(query4,[balance1,aidt])
            self.success("Done","Transaction successfull")
            mydb.commit()
        else:
            self.error("Warning","Low Balance")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Amount1 = QtWidgets.QLabel(Dialog)
        self.Amount1.setGeometry(QtCore.QRect(50, 80, 121, 21))
        self.Amount1.setObjectName("Amount1")
        self.Account = QtWidgets.QLabel(Dialog)
        self.Account.setGeometry(QtCore.QRect(50, 140, 141, 21))
        self.Account.setObjectName("Account")
        self.Amount1text = QtWidgets.QLineEdit(Dialog)
        self.Amount1text.setGeometry(QtCore.QRect(200, 80, 151, 31))
        self.Amount1text.setObjectName("Amount1text")
        self.Accounttext = QtWidgets.QLineEdit(Dialog)
        self.Accounttext.setGeometry(QtCore.QRect(200, 140, 151, 31))
        self.Accounttext.setObjectName("Accounttext")
        self.Transfer = QtWidgets.QPushButton(Dialog)
        self.Transfer.setGeometry(QtCore.QRect(140, 200, 106, 30))
        self.Transfer.setObjectName("Transfer")
        self.Transfer.clicked.connect(self.trans)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Transfer"))
        self.Amount1.setText(_translate("Dialog", "Enter Amount"))
        self.Account.setText(_translate("Dialog", "Enter Account ID"))
        self.Transfer.setText(_translate("Dialog", "Transfer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Transfer()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

