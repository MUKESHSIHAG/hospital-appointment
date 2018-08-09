#update the appointments
from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master

        #heading label
        self.heading = Label(master, text = 'update Appointments', fg='lightgreen', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        #search critaria
        self.name = Label(master, text="Enter Patient's Name", font=('srial 20 bold'))
        self.name.place(x=0,y=60)

        #entry for the name.......
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=290, y=67)

        #search button
        self.search = Button(master, text='search', width=12, height=1, bg='steelblue')
        self.search.place(x=350, y=102)

    #function to search
    def search_db(self):
        self.input = self.namenet.get()
        #execute sql
        sql = "SELECT * FROM appointments WHERE name LIKE?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.row():
            self.name = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        #creating the update form
        self.unname = Label(self.master, text="Patient's Name", font=('arial 40 bold'))
        self.unname.place(x=0, y=140)

        self.unage = Label(self.master, text="Age", font=('arial 40 bold'))
        self.unage.place(x=0, y=180)

        self.ungender = Label(self.master, text="Gender", font=('arial 40 bold'))
        self.ungender.place(x=0, y=220)

        self.unlocation = Label(self.master, text="Location", font=('arial 40 bold'))
        self.unlocation.place(x=0, y=260)

        self.untime = Label(self.master, text="Time", font=('arial 40 bold'))
        self.untime.place(x=0, y=300)

        self.unphone = Label(self.master, text="Phone", font=('arial 40 bold'))
        self.unphone.place(x=0, y=340)

        #creating th entries
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))
        
        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))
        
        #button to execute update
        self.update = Button(self.master, text="update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=380, y=380)

        #button to delete
        self.delete = Button(self.master, text="update", width=20, height=2, bg='lightblue', command=self.delete_db)
        self.delete.place(x=380, y=380)
    
    def update_db(self):
        self.var1 = self.ent1.get()
        self.var2 = self.ent2.get()
        self.var3 = self.ent3.get()
        self.var4 = self.ent4.get()
        self.var5 = self.ent5.get()
        self.var6 = self.ent6.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?,Phone=?, time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.varr2, self.var3, self.var4, self.var5, self.var6, self.namenet.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Updated"," successfully updated")

    def delete_db(self):
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfow("Success", "successfully deleted")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()

#creating the object
root  = Tk()
b = Application(root)
root.geometry("1280x720+0+0")
root.resizable(FALSE,FALSE)
root.mainloop()