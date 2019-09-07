# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Withdraw import Ui_Dialog1
from Deposit import Ui_Dialog2
from Transfer import Ui_Transfer
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

class Ui_Options(object):
    mycursor=mydb.cursor()
    def __init__(self,username):
        self.username=username
    def wit(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog1(self.username)
        self.ui.setupUi(self.window)
        self.window.show()
  
    def dep(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog2(self.username)
        self.ui.setupUi(self.window)
        self.window.show()        

    def tran(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Transfer(self.username)
        self.ui.setupUi(self.window)
        self.window.show()

    def check1(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(self.message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def check2(self):
        aid=self.username
        exe1="Select BALANCE from ACCOUNT where AID=%s"
        mycursor.execute(exe1,[aid])
        X=mycursor.fetchall()
        bala=int(X[0][0])
        self.check1("Current Balace",bala)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 443)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 170, 80, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 230, 80, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 280, 80, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 340, 80, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 160, 106, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.wit)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 220, 106, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.dep)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 280, 106, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.tran)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 340, 106, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.check1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 50, 111, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Option"))
        self.label.setText(_translate("Dialog", "1"))
        self.label_2.setText(_translate("Dialog", "2"))
        self.label_3.setText(_translate("Dialog", "3"))
        self.label_5.setText(_translate("Dialog", "4"))
        self.pushButton.setText(_translate("Dialog", "Withdraw"))
        self.pushButton_2.setText(_translate("Dialog", "Deposit"))
        self.pushButton_3.setText(_translate("Dialog", "Transfer"))
        self.pushButton_4.setText(_translate("Dialog","Balance"))
        self.label_4.setText(_translate("Dialog", "Select Option"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Options()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

