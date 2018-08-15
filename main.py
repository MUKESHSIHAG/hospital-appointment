from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x500")
root.title("Registration Form")

Fullname = StringVar()
Email = StringVar()
var = IntVar()
c = IntVar()
var1 = IntVar()

def database():
    name1 = Fullname.get()
    email = Email.get()
    gender = var.get()
    country = c.get()
    prog = var1.get()
    conn = sqlite3.connect('learn.db')
    with conn:
        cursor = conn.cursor
    conn.execute('CREATE TABLE IF NOT EXISTS Student(Fullname TEXT,Email TEXT,Gender TEXT,Country TEXT,Programming TEXT)')
    conn.execute('INSERT INTO Student(Fullname,Email,Gender,Country,Programming)VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
    conn.commit()

label_0 = Label(root, text="Registration Form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root,width=30)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root,width=30)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

label_4 = Label(root, text="Country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

list1 = ['India','Canada','USA','England','Nepal','Pakistan','Japan','China','Russia']
c = StringVar()
droplist = OptionMenu(root,c,*list1)
droplist.config(width=20)
c.set('Select Your Country')
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming", width=20, font=("bold",10))
label_4.place(x=85, y=330)
var1 = IntVar()
Checkbutton(root,text='java',variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root,text='python',variable=var2).place(x=290,y=330)

Button(root,text='Submit',width=15,bg='brown',fg='black',command = database).place(x=180,y=400)

mainloop()