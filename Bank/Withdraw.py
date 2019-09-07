# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Withdraw.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

class Ui_Dialog1(object):
    def error(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def success(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def __init__(self ,username):
        self.username=username
    def get(self):
        amt=int(self.Amounttext.text())
        mycursor=mydb.cursor()
        aid=self.username
        lan="select BALANCE from ACCOUNT where AID=%s"
        mycursor.execute(lan,[aid])
        b=mycursor.fetchall()
        balance=int(b[0][0])
        if 0<amt and amt<balance:
            balance=int(balance)-int(amt)
            new="Update ACCOUNT SET BALANCE=%s where AID=%s"
            mycursor.execute(new,[balance,aid])
            mydb.commit()
            self.success("Done","Transaction successfull")
        else:
            self.error("Error","Check Withdrawal amount")
            
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Amount = QtWidgets.QLabel(Dialog)
        self.Amount.setGeometry(QtCore.QRect(30, 90, 121, 21))
        self.Amount.setObjectName("Amount")
        self.Amounttext = QtWidgets.QLineEdit(Dialog)
        self.Amounttext.setGeometry(QtCore.QRect(180, 90, 121, 31))
        self.Amounttext.setObjectName("Amounttext")
        self.Withdraw = QtWidgets.QPushButton(Dialog)
        self.Withdraw.setGeometry(QtCore.QRect(120, 160, 106, 30))
        self.Withdraw.setObjectName("Withdraw")
        self.Withdraw.clicked.connect(self.get)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Withdrawal"))
        self.Amount.setText(_translate("Dialog", "Enter Amount"))
        self.Withdraw.setText(_translate("Dialog", "Withdraw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

