#import module
from tkinter import *
import sqlite3
import tkinter.messagebox



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

        self.age = Label(self.left, text="Age", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.age.place(x=0, y=140)

        self.gender = Label(self.left, text="Gender", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.gender.place(x=0, y=180)

        self.location = Label(self.left, text="Location", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.location.place(x=0, y=220)

        self.time = Label(self.left, text="Appointment Time", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.time.place(x=0, y=260)

        self.phone = Label(self.left, text="Phone Number", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.phone.place(x=0, y=300)
        
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

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        #button to perform command................
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='lightgreen', command = self.add_appointment)
        self.submit.place(x=285, y=340)

    #function to call when the submit button i  s clicked.........
    def add_appointment(self):
        #getting the user input..........
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        
        #checking if the users input is empty.......
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo('warning', 'please fill up the form')
        else:
            #now we add it to the database.......
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled-time, phone)VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            print("successful")
        

#creating the object
root = Tk()
b = Application(root)

#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False,False)

#end the loop
root.mainloop()