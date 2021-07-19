from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from fitness_tools.meals.meal_maker import MakeMeal
conn = sqlite3.connect("main.db")#main database conn.
cursor=conn.cursor()


def accwindow():

        def windows():
            def editprofile():
                def ok():
                    nc = conn.cursor()
                    sql = 'select Name from accdetails where email=?'
                    cursor.execute(sql, (email,))
                    row = cursor.fetchall()
                    conn.commit()
                    row1 = row[0]
                    finaln = row1[0]
                    strname = str(finaln)
                    nmem = sqlite3.connect(email + ".db")
                    ncursor = nmem.cursor()
                    sqlite_insert_with_param = """INSERT INTO userprofile
                                              (NAME,AGE,WEIGHT,BODYTYPE,GENDER,WORK) 
                                              VALUES (?, ?, ?, ?, ?, ?);"""

                    data_tuple = (strname, age.get(), weight.get(), b.get(), g.get(), w.get())
                    ncursor.execute(sqlite_insert_with_param, data_tuple)
                    nmem.commit()

                    obj = MakeMeal(weight.get(), goal=g.get(), activity_level=w.get(),
                                   body_type=b.get())
                    ncursor = nmem.cursor()
                    sqlite_insert_with_param = """INSERT INTO macros
                                                          (NAME,CALORIES,WEIGHT,CARBS,PROTEIN,FATS) 
                                                          VALUES (?, ?, ?, ?, ?, ?);"""

                    data_tuple = (
                    strname, obj.daily_min_calories(), weight.get(), obj.daily_min_carbs(), obj.daily_min_protein(),
                    obj.daily_min_fat())
                    ncursor.execute(sqlite_insert_with_param, data_tuple)
                    nmem.commit()

                edit = Toplevel()
                edit.geometry('400x400')
                edit['bg'] = 'gray63'
                edit.title('Update Profile')
                work = ['very active', 'moderate', 'Little to no']
                bodytype = ['endomorph', 'ectomorph', 'mesomorph']
                goal = ['weight_loss', 'maintenance', 'weight_gain']
                age = IntVar()
                weight = IntVar()
                b = StringVar()
                g = StringVar()
                w = StringVar()
                Label(edit, text='Enter Details', font='Helvetica 12 bold', bg='gray63').grid(row=1, column=1)










                Label(edit, text='Enter client details:', bg='gray63').grid(row=3, column=1)
                Label(edit, text='AGE', bg='gray63').grid(row=4, column=1)
                Entry(edit, width=15, textvariable=age).grid(row=4, column=2)

                Label(edit, text='WEIGHT(lbs)', bg='gray63').grid(row=5, column=1)
                Entry(edit, width=15, textvariable=weight).grid(row=5, column=2)
                Label(edit, text='BODY TYPE', bg='gray63').grid(row=6, column=1)
                classselect = ttk.Combobox(edit, values=bodytype, state='readonly', textvariable=b)
                classselect.grid(row=6, column=2)
                Label(edit, text='GOAL', bg='gray63').grid(row=7, column=1)
                classselect = ttk.Combobox(edit, values=goal, state='readonly', textvariable=g)
                classselect.grid(row=7, column=2)
                Label(edit, text='WORK', bg='steel blue').grid(row=8, column=2)
                classselect = ttk.Combobox(edit, values=work, state='readonly', textvariable=w)
                classselect.grid(row=9, column=2)
                Button(edit, text='EDIT', command=ok).grid(row=10, column=2)

            def accwindow1():
                cprofile.destroy()
                windows()
            cprofile = Toplevel()  # class-profile-GUI
            cprofile.geometry('1100x700')
            cprofile.title('clientprofile-CMS')
            cprofile['bg'] = 'gray63'

            Button(cprofile, text='Refresh', command=accwindow1, bg='steel blue').place(x=860, y=11)
            Button(cprofile, text='Edit Profile', command=editprofile, bg='steel blue').place(x=860, y=69)
            Label(cprofile, text='Client Details', bg='gray63', font='Helvetica 12 bold').grid(row=3, column=2)

            # student details
            scroll = ttk.Scrollbar(cprofile)
            scroll.grid(row=4, column=3)
            tb = ttk.Treeview(cprofile, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', selectmode='browse')
            tb.grid(row=4, column=2)

            tb.heading(1, text="Month")
            tb.column(1, minwidth=0, width=50, stretch=NO)
            tb.heading(2, text="Name")
            tb.column(2, minwidth=0, width=120, stretch=NO)
            tb.heading(3, text="Calories")
            tb.column(3, minwidth=0, width=50, stretch=NO)
            tb.heading(4, text="Carbs")
            tb.column(4, minwidth=0, width=50, stretch=NO)
            tb.heading(5, text="Protein")
            tb.column(5, minwidth=0, width=80, stretch=NO)
            tb.heading(6, text="Fats")
            tb.column(6, minwidth=0, width=50, stretch=NO)
            tb.heading(7, text="Weight(lbs)")
            tb.column(7, minwidth=0, width=50, stretch=NO)
            scroll.config(command=tb.yview)
            #########################################################################################
            data = sqlite3.connect(email + ".db")
            ncursor = data.cursor()
            ncursor.execute('select * from macros;')
            rows = ncursor.fetchall()
            for i in rows:
                tb.insert('', 'end', values=i)

        windows()



def sign():
    def proceed1():
        global email
        email = em.get()
        passwo = pas.get()
        check = [(email, passwo)]
        pre = conn.cursor()
        pre.execute('select email,password from accdetails;')
        row = pre.fetchall()
        flag = 0
        for i in range(len(row)):
            if row[i] == check[0]:
                flag = 1
        if flag == 0:
            return messagebox.showerror('Error', 'Email/Password is Incorrect')
        else:
            sign.destroy()
            accwindow()


    def account():  # newaccount
        sign.destroy()

        def proceed():
            name = n.get()
            email = e.get()
            passw = p.get()
            if name == '':
                return messagebox.showerror('Error', 'Enter Name')
            elif email == '':
                return messagebox.showerror('Error', 'Enter email')
            elif passw == '':
                return messagebox.showerror('Error', 'Enter  Password')
            else:
                nc = conn.cursor()
                sqlite_insert_with_param = """INSERT INTO accdetails
                          (email,password,Name) 
                          VALUES (?, ?, ?);"""
                data_tuple = (email, passw, name)
                nc.execute(sqlite_insert_with_param, data_tuple)
                conn.commit()
                nmem = sqlite3.connect(email + ".db")
                ncursor = nmem.cursor()  # cursor for selected class
                ncursor.execute(
                """CREATE TABLE userprofile (NO INTEGER PRIMARY KEY,NAME TEXT,AGE INTEGER,WEIGHT INTEGER,BODYTYPE TEXT,GENDER TEXT,WORK INTEGER)""")
                ncursor.execute(
                    """CREATE TABLE macros (NO INTEGER PRIMARY KEY,NAME TEXT,CALORIES INTEGER,WEIGHT INTEGER,CARBS INTEGER,PROTEIN INTEGER ,FATS INTEGER)""")
                # table for student details
                nmem.close()
                messagebox.showinfo('Data', 'Registered Successfully')

        n = StringVar()
        e = StringVar()
        p = StringVar()
        new = Toplevel()
        new.title('Create Account')
        new.geometry('400x400')
        new['bg'] = 'gray63'
        Label(new, text='Enter Details', font='Helvetica 12 bold', bg='gray63').grid(row=1, column=2)
        Label(new, text='Enter Full Name', bg='gray63').grid(row=2, column=1)
        Entry(new, width=25, textvariable=n).grid(row=2, column=2)  # name
        Label(new, text='Enter Email', bg='gray63').grid(row=3, column=1)
        Entry(new, width=25, textvariable=e).grid(row=3, column=2)  # email
        Label(new, text='Enter New Password', bg='gray63').grid(row=4, column=1)
        Entry(new, width=25, textvariable=p, show='*').grid(row=4, column=2)  # password
        Button(new, text='Proceed', command=proceed, bg='steel blue').grid(row=5, column=3)

    em = StringVar()
    pas = StringVar()
    sign = Toplevel()
    sign.title('SignIn/CreateAccount-CMS')
    sign.geometry('400x400')
    sign['bg'] = 'gray63'
    Label(sign, text='Sign In', font='Helvetica 12 bold', bg='gray63').grid(row=1, column=2)
    Button(sign, text='CreateAccount', command=account, bg='steel blue').grid(row=1, column=3)
    Label(sign, text='Enter Email Address:', bg='gray63').grid(row=2, column=1)
    Entry(sign, width=25, textvariable=em).grid(row=2, column=2)  # email
    Label(sign, text='Enter Password', bg='gray63').grid(row=3, column=1)
    Entry(sign, width=25, textvariable=pas, show='*').grid(row=3, column=2)  # password
    Button(sign, text='Proceed', command=proceed1, bg='steel blue').grid(row=4, column=3)


########################################################################################
home = Tk()
home['bg'] = 'gray63'
home.geometry('480x300')
home.title('Calorie Management System')
Label(home, text='---HOME PAGE---', font='Helvetica 12 bold', bg='gray63').place(relx=0.37, rely=0.1)
Button(home, text='SignIn/Create Account', command=sign, bg='steel blue').place(relx=0.37, rely=0.2)
home.mainloop()