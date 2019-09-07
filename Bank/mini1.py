import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="sourav2",password="souravmudaliar19620",database="Bank")

mycursor =mydb.cursor()

mycursor.execute("select * from CUSTOMERS");

L=mycursor.fetchall()
print(L)



    def messagebox(self,title,message):
		mess=QtWidgets.QMessagebox()
		mess=setWindowTitle(title)
		mess.setStandardButtons(QtWidgets.QMessagebox.OK)
		mess.execute()

	def warning(self,title,message):
		mess=QtWidgets.QMessagebox()
		mess=setWindowTitle(title)
		mess.setStandardButtons(QtWidgets.QMessagebox.OK)
		mess.execute()	

	def login(self):
		Name=self.textEdit.text()
		Password=self.textEdit_2.text()
		cur=mydb.cursor()
		query="select * from CUSTOMERS where NAME=%s and PASSWORD=%s"
		data=cur.execute(query,(NAME,PASSWORD))
		if(len(cur.fetchall())>0):
			self.messagebox("Hey","Login Successful")
		else:
			self.warning("Warning","Incorrect Name or Password")




			self.Login.clicked.connect(self.login)