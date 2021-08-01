import tkinter as tk
import mysql.connector
import tkinter.messagebox
def submitact():
	user = Username.get()
	passw = password.get()
	print("Entered Credentials:\nUser: ", user, "\nPassword: ", len(passw) * '*', '\n')
	logintodb(user, passw)

def logintodb(user, passw):
	global cursor, db
	if passw:
		db = mysql.connector.connect(host="localhost", user=user, password=passw, db="my_db")
		cursor = db.cursor()
	savequery = "select * from Product"

	try:
		cursor.execute(savequery)
		myresult = cursor.fetchall()
		for x in myresult:
			print(x)
		print("Database Extracted Successfully")
	except:
		db.rollback()
		print("Error: Invalid User")

def valid():
	tk.messagebox.showinfo("Verify User","VERIFIED!!!VALID USER")
root = tk.Tk()
root.geometry("400x300")
root.title("Database Login")

lblfrstrow = tk.Label(root, text="Username -")
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login", bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

verbtn = tk.Button(root, text="Verify", bg="blue", command=valid)
verbtn.place(x=280, y=135, width=55)
root.mainloop()
