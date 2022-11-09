from tkinter import *
from tkinter import messagebox
import pymysql


windows = Tk()
windows.geometry('530x490+220+10')
windows.resizable(False, False)
windows.title('Change Password')
from tkinter import messagebox
import pymysql

def submit():
    if nameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All entry fields must be entered')
        return
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Passwords do not match')
        return
    else:
         db = pymysql.connect(host='localhost', user='root', password='1234', database='change_password')
         cur=db.cursor()
         query='select * from change_p where firstname=%s'
         cur.execute(query, (nameEntry.get()))
         data=cur.fetchone() #to fetch for an existing data

         if data == None:
            messagebox.showerror('Error','The name does not exist')
         else:
            query = 'update change_p set password=%s where firstname = %s'
            cur.execute(query, (passwordEntry.get(), nameEntry.get()))
            db.commit() #update
            db.close()
            messagebox.showinfo('Successful', 'Successful Changes')

            nameEntry.delete(0,END)
            passwordEntry.delete(0, END)
            confirmpasswordEntry.delete(0, END)





frame=Frame(windows, width=530, height=490, bg='#FFFFF5', bd=8)
frame.place(x=0, y=0)

heading = Label(frame, text='Change Password', fg='Black', bg='#FFFFF5', font=('Calibre', 22, 'bold'))
heading.place(x=100, y=5)

nameLabel=Label(frame, text='Name:', fg='black', bg='#FFFFF5', font=('Calibre', 18, 'bold'))
nameLabel.place(x=10, y=90)

nameEntry=Entry(frame, width=33, borderwidth=4)
nameEntry.place(x=260, y=90)

passwordLabel=Label(frame, text='Password:', fg='black', bg='#FFFFF5', font=('Calibre', 18, 'bold'))
passwordLabel.place(x=10, y=140)

passwordEntry=Entry(frame, width=33, borderwidth=4)
passwordEntry.place(x=260, y=140)

confirmpasswordLabel=Label(frame, text='Confirm Password:', fg='black', bg='#FFFFF5', font=('Calibre', 18, 'bold'))
confirmpasswordLabel.place(x=10, y=190)

confirmpasswordEntry=Entry(frame, width=33, borderwidth=4)
confirmpasswordEntry.place(x=260, y=190)

submitbtn=Button(frame, text='Submit', font=('Calibre', 18, 'italic bold'), width=20, height=2, bg='#7f7fff', fg='black',cursor='hand2', border=4, command=submit)
submitbtn.place(x=100, y=280)





windows.mainloop()
