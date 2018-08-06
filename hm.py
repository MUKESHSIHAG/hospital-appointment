#import module
from tkinter import *
import sqlite3

#content for database
conn = sqlite3.connect('database.db')
#cursor to move around database
c = conn.cursor()

#tkinter window
class Application:
    def __init__(self,master):
        self.master = master

        #creating frames in master
        self.left = Frame(master, width=800, height=720, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='lightgreen')
        self.right.pack(side=RIGHT)
        
        #labels for the window
        self.heading = Label(self.left, text="MKS Hospital Appointment", font=('arial 40 bold'), fg='white', bg='lightblue')
        self.heading.place(x=0, y=0)

        self.name = Label(self.left, text="Patient's Name", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.name.place(x=0, y=100)

        self.age = Label(self.left, text="Age", font=('arial 20 bold'), fg='balck', bg='lightblue')
        self.age.place(x=0, y=140)

        self.gender = Label(self.left, text="Gender", font=('arial 20 bold'), fg='balck', bg='lightblue')
        self.gender.place(x=0, y=180)

        self.location = Label(self.left, text="Location", font=('arial 20 bold'), fg='balck', bg='lightblue')
        self.location.place(x=0, y=220)

        self.time = Label(self.left, text="Appointment Time", font=('arial 20 bold'), fg='balck', bg='lightblue')
        self.time.place(x=0, y=260)
        
        #taking the entries.................
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        #button to perform command................
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='lightgreen')
        self.submit.place(x=300, y=3005)

#creating the object
root = Tk()
b = Application(root)

#resolution of the window
root=geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False,False)

#end the loop
root.mainloop()