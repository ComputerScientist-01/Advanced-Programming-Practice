import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

from tkinter import messagebox


def Database():
    fnm = fname.get()
    lnm = lname.get()
    d = date.get()
    m = month.get()
    y = year.get()
    em = email.get()
    mob = mobn.get()
    gend = gender.get()
    adds = address.get()
    add1 = ad1.get()
    ct = city.get()
    pinc = pin.get()
    st = state.get()
    cout = country.get()
    hob = hobby.get()
    othr = other.get()
    b11 = b1.get()
    b22 = b2.get()
    b33 = b3.get()
    b44 = b4.get()
    p11 = p1.get()
    p22 = p2.get()
    p33 = p3.get()
    p44 = p4.get()
    y11 = y1.get()
    y22 = y2.get()
    y33 = y3.get()
    y44 = y4.get()

    db = sqlite3.connect('stform3.db')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS STFORM3(fname TEXT,lname TEXT,date INT,month TEXT,year INT,email TEXT,mobn INT,gender TEXT,address TEXT,ad1 TEXT,city TEXT,pin INT,state TEXT,country TEXT,hobby TEXT,other TEXT,b1 TEXT,b2 TEXT,b3 TEXT,b4 TEXT,p1 INT,p2 INT,p3 INT,p4 INT,y1 INT,y2 INT,y3 INT,y4 INT)')
    cursor.execute('INSERT INTO STFORM3(fname,lname,date,month,year,email,mobn,gender,address,ad1,city,pin,state,country,hobby,other,b1,b2,b3,b4,p1,p2,p3,p4,y1,y2,y3,y4) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   (fnm, lnm, d, m, y, em, mob, gend, adds, add1, ct, pinc, st, cout, hob, othr, b11, b22, b33, b44, p11, p22, p33, p44, y11, y22, y33, y44))
    db.commit()
    msg = messagebox.showinfo("Sent To Database", "SUBMITTED SUCCESSFULLY")


def display():
    db = sqlite3.connect('stform3.db')
    with db:
        cursor = db.cursor()
        window = ttk.Tk()
        window.geometry("400x250")

    select = cursor.execute('''SELECT * from STFORM3 ''')
    i = 0
    for STFORM3 in select:
        for j in range(len(STFORM3)):
            e = Entry(my_w, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, STFORM3[j])
        i = i+1


an = Tk()
an.geometry("1100x900")

an.title("Student Registration Form")
an.configure(background="Purple")


fname = Label(an, text="FIRST NAME: ",
              font=("Calibri", 12)).place(x=100, y=60)
fname = Entry(an, width=20)
fname.place(x=300, y=63)
maxc = Label(an, text="(Max 30 charcters only a-z or A-Z)",
             font=("Calibri", 8)).place(x=550, y=63)

lname = Label(an, text="LAST NAME: ", font=("Calibri", 12)).place(x=100, y=90)
lname = Entry(an, width=20)
lname.place(x=300, y=93)

maxn = Label(an, text="(Max 30 charcters only a-z or A-Z)",
             font=("Calibri", 8)).place(x=550, y=93)

dob = Label(an, text="DATE OF BIRTH:",
            font=("Calibri", 12)).place(x=100, y=120)
date = ttk.Combobox(an, text="Date", width=5)
date['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
date.place(x=300, y=123)

month = ttk.Combobox(an, text="Month", width=5)
month['values'] = ("JAN(1)", "FEB(2)", "MAR(3)", "APR(4)", "MAY(5)",
                   "JUN(6)", "JUL(7)", "AUG(8)", "SEP(9)", "OCT(10)", "NOV(11)", "DEC(12)")
month.place(x=400, y=123)

year = ttk.Combobox(an, text="Year", width=5)
year['values'] = (1995, 1996, 1997, 1998, 1999,
                  2000, 2001, 2002, 2003, 2004, 2005)
year.place(x=500, y=123)

email = Label(an, text="EMAIL ID: ", font=("Calibri", 12)).place(x=100, y=150)
email = Entry(an, width=40)
email.place(x=300, y=153)

mobn = Label(an, text="MOBILE NUMBER: ",
             font=("Calibri", 12)).place(x=100, y=180)
mobn = Entry(an, width=20)
mobn.place(x=300, y=183)
maxd = Label(an, text="(Max 10 numbers only 0-10)",
             font=("Calibri", 8)).place(x=550, y=183)

gen = Label(an, text="GENDER: ", font=("Calibri", 12)).place(x=100, y=210)
gender = ttk.Combobox(an, text="Gender", width=10)
gender['values'] = ("Male", "Female", "Others")
gender.place(x=300, y=212)

address = Label(an, text="ADDRESS: ",
                font=("Calibri", 12)).place(x=100, y=240)
address = Entry(an, width=40)
address.place(x=300, y=243)

ad1 = Entry(an, width=40)
ad1.place(x=300, y=273)

city = Label(an, text="CITY:", font=("Calibri", 12)).place(x=100, y=300)
city = Entry(an, width=30)
city.place(x=300, y=303)

pin = Label(an, text="PINCODE: ", font=("Calibri", 12)).place(x=100, y=330)
pin = Entry(an, width=30)
pin.place(x=300, y=333)

state = Label(an, text="STATE: ", font=("Calibri", 12)).place(x=100, y=360)
state = Entry(an, width=30)
state.place(x=300, y=363)

country = Label(an, text="COUNTRY: ",
                font=("Calibri", 12)).place(x=100, y=390)
country = Entry(an, width=30)
country.place(x=300, y=393)

hobby = Label(an, text="HOBBIES: ", font=("Calibri", 12)).place(x=100, y=420)
hobby = ttk.Combobox(an, text="Hobbies", width=29)
hobby['values'] = ("DRAWING ", "SKETCHING ", "DANCING ")
hobby.place(x=300, y=420)

oth = Label(an, text="OTHER").place(x=250, y=450)
other = Entry(an, width=20)
other.place(x=320, y=450)

qua = Label(an, text="QUALIFICATION: ",
            font=("Calibri", 12)).place(x=100, y=490)
si = Label(an, text="SR.NO ", font=("Calibri", 12)).place(x=250, y=520)
exam = Label(an, text="EXAMINATION", font=("Calibri", 12)).place(x=330, y=520)
board = Label(an, text="BOARD", font=("Calibri", 12)).place(x=495, y=520)
per = Label(an, text="SCORE", font=("Calibri", 12)).place(x=630, y=520)
yop = Label(an, text="YEAR", font=(
    "Calibri", 12)).place(x=765, y=520)

one = Label(an, text="1", font=("Calibri", 12)).place(x=260, y=550)
sec = Label(an, text="2", font=("Calibri", 12)).place(x=260, y=580)
trd = Label(an, text="3", font=("Calibri", 12)).place(x=260, y=610)
four = Label(an, text="4", font=("Calibri", 12)).place(x=260, y=640)

ten = Label(an, text="CLASS X", font=("Calibri", 12)).place(x=340, y=550)
twe = Label(an, text="CLASS XII", font=("Calibri", 12)).place(x=340, y=580)
grad = Label(an, text="GRADUATION", font=("Calibri", 12)).place(x=340, y=610)
mast = Label(an, text="MASTERS", font=("Calibri", 12)).place(x=340, y=640)


b1 = Entry(an, width=10)
b1.place(x=495, y=550)
b2 = Entry(an, width=10)
b2.place(x=495, y=580)
b3 = Entry(an, width=10)
b3.place(x=495, y=610)
b4 = Entry(an, width=10)
b4.place(x=495, y=640)

p1 = Entry(an, width=10)
p1.place(x=630, y=550)
p2 = Entry(an, width=10)
p2.place(x=630, y=580)
p3 = Entry(an, width=10)
p3.place(x=630, y=610)
p4 = Entry(an, width=10)
p4.place(x=630, y=640)

y1 = Entry(an, width=10)
y1.place(x=765, y=550)
y2 = Entry(an, width=10)
y2.place(x=765, y=580)
y3 = Entry(an, width=10)
y3.place(x=765, y=610)
y4 = Entry(an, width=10)
y4.place(x=765, y=640)

caf = Label(an, text="APPLY COURSE:",
            font=("Calibri", 12)).place(x=100, y=675)

bca = ttk.Radiobutton(an, text="BCA ", value=1).place(x=275, y=676)
bcom = ttk.Radiobutton(an, text="BCOM ", value=2).place(x=350, y=676)
bsc = ttk.Radiobutton(an, text="BSC ", value=3).place(x=445, y=676)
ba = ttk.Radiobutton(an, text="BA ", value=4).place(x=520, y=676)


msg = Button(an, text="SUBMIT", width=10, command=Database).place(x=100, y=730)


an.mainloop()
