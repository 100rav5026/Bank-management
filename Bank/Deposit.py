# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Deposit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

class Ui_Dialog2(object):
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
    def put(self):
        amt=int(self.Amounttext2.text())
        mycursor=mydb.cursor()
        aid=self.username
        lan="select BALANCE from ACCOUNT where AID=%s"
        mycursor.execute(lan,[aid])
        b=mycursor.fetchall()
        balance=int(b[0][0])
        if 0<amt:
            balance=int(balance)+int(amt)
            new="Update ACCOUNT SET BALANCE=%s where AID=%s"
            mycursor.execute(new,[balance,aid])
            mydb.commit()
            self.success("Done","Transaction successfull")
        else:
            self.error("Error","Invalid Deposit amount")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Amount1 = QtWidgets.QLabel(Dialog)
        self.Amount1.setGeometry(QtCore.QRect(50, 90, 121, 21))
        self.Amount1.setObjectName("Amount1")
        self.Amounttext2 = QtWidgets.QLineEdit(Dialog)
        self.Amounttext2.setGeometry(QtCore.QRect(200, 90, 104, 31))
        self.Amounttext2.setObjectName("Amounttext2")
        self.Deposit = QtWidgets.QPushButton(Dialog)
        self.Deposit.setGeometry(QtCore.QRect(130, 170, 106, 30))
        self.Deposit.setObjectName("Deposit")
        self.Deposit.clicked.connect(self.put)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Deposit"))
        self.Amount1.setText(_translate("Dialog", "Enter Amount"))
        self.Deposit.setText(_translate("Dialog", "Deposit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

