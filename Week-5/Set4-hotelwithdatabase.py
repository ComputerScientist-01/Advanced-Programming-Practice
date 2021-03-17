from tkinter import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox


window = Tk()
window.title("Hotel Room Booking Form")
window.geometry('1500x800')
window.configure(background = "white");


a1=StringVar()
b1=StringVar()
c1=StringVar()
d1=StringVar()
e1=IntVar()
f1=IntVar()
g1=StringVar()
h1=StringVar()
i1=StringVar()
j1=StringVar()
k1=IntVar()
l1=StringVar()
m1=IntVar()
p101=StringVar()
p102=StringVar()
p103=StringVar()

def database():
    title=a1.get()
    fname=b1.get()
    lname=c1.get()
    share=d1.get()
    busno=e1.get()
    mobno=f1.get()
    email=g1.get()
    doa=h1.get()
    dod=i1.get()
    nmcred=j1.get()
    credno=k1.get()
    expd=l1.get()
    cvv=m1.get()
    sign=p101.get()
    date=p102.get()
    pname=p103.get()
    
    db = sqlite3.connect('hotel.db')
    cursor=db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS HOTEL(a1 TEXT,b1 TEXT,c1 TEXT,d1 TEXT,e1 INT,f1 INT,g1 TEXT,h1 TEXT,i1 TEXT,j1 TEXT,k1 INT,l1 TEXT,m1 INT,p101 TEXT,p102 TEXT,p103 TEXT)')
    cursor.execute('INSERT INTO HOTEL(a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,p101,p102,p103) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (title,fname,lname,share,busno,mobno,email,doa,dod,nmcred,credno,expd,cvv,sign,date,pname))
    db.commit()
    msg = messagebox.showinfo( "DB Demo","SUBMITTED SUCCESSFULLY")
    
    
def display():
    db=sqlite3.connect('hotel.db')
    
    with db:
        cursor=db.cursor()
        my_w = tk.Tk()
        my_w.geometry("600x250") 

        r_set=cursor.execute('''SELECT * from HOTEL ''');
        i=0  
        for HOTEL in r_set: 
            for j in range(len(HOTEL)):
                e = Entry(my_w, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, HOTEL[j])
            i=i+1
a = Label(window ,text = "Title ").grid(row = 0,column = 0,sticky = "NSEW")
b = Label(window ,text = "First Name ").grid(row = 1,column = 0,sticky = "NSEW")
c = Label(window ,text = "Last Name ").grid(row = 2,column = 0,sticky = "NSEW")
d = Label(window ,text = "Share With ").grid(row = 3,column = 0,sticky = "NSEW")
e = Label(window ,text = "Buisness Number ").grid(row = 4,column = 0,sticky = "NSEW")
f = Label(window ,text = "Mobile Number").grid(row = 5,column = 0,sticky = "NSEW")
g = Label(window ,text = "Email Address ").grid(row = 6,column = 0,sticky = "NSEW")
h = Label(window ,text = "Date of Arrival ").grid(row = 7,column = 0,sticky = "NSEW")
i = Label(window ,text = "Date of Departure ").grid(row = 8,column = 0,sticky = "NSEW")
j = Label(window ,text = "Name on Credit Card ").grid(row = 9,column = 0,sticky = "NSEW")
k = Label(window ,text = "Credit Card Number ").grid(row = 10,column = 0,sticky = "NSEW")
l = Label(window ,text = "Expiry Date ").grid(row = 11,column = 0,sticky = "NSEW")
m = Label(window ,text = "CVV Number ").grid(row = 12,column = 0,sticky = "NSEW")
n = Label(window ,text = "Payment Method ").grid(row = 13,column = 0,sticky = "NSEW")
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(window, text = "Credit Card ", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C1.grid(row = 13, column = 1 , sticky = "NSEW")
C2 = Checkbutton(window, text = "Debit Bank Transfer ", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C2.grid(row = 13, column = 2 , sticky = "NSEW")
p = Label(window ,text = "Negotiated Rates : ").grid(row = 14,column = 0 , sticky = "NSEW")
g = Label(window ,text = "Deluxe Room Single ").grid(row = 15,column = 0 , sticky = "NSEW")
g1 = Label(window ,text = " R1700 ").grid(row = 15,column = 1 , sticky = "NSEW")
h = Label(window ,text = "Deluxe Room Double ").grid(row = 15,column = 2 , sticky = "NSEW")
h1 = Label(window ,text = " R1700 ").grid(row = 15,column = 3 , sticky = "NSEW")
g = Label(window ,text = "Suites Room Single ").grid(row = 16,column = 0 , sticky = "NSEW")
g1 = Label(window ,text = " R1700 ").grid(row = 16,column = 1 , sticky = "NSEW")
h = Label(window ,text = "Suites Room Double ").grid(row = 16,column = 2,sticky = "NSEW")
h1 = Label(window ,text = " R1700 ").grid(row = 16,column = 3 ,sticky = "NSEW")
p1 = Label(window ,text = "Room Preference : ").grid(row = 17,column = 0,sticky = "NSEW")
CheckVar11 = IntVar()
CheckVar22 = IntVar()
C3 = Checkbutton(window, text = "King Bed ", variable = CheckVar11, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C3.grid(row = 18, column = 0)
C4 = Checkbutton(window, text = "Twin - Two Single Beds ", variable = CheckVar22, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C4.grid(row = 18, column = 1)

line1 = Label(window, text="The above rates are quoted per room, per night. The rates include breakfast, 14% vat, and Excludes 1% Tourism Levy\n and a voluntary R10 donation to the Arabella Community Trust that will be levies onto your account.", bg="white")
line2 = Label(window, text="Total amount payable      ZAR__ x_ nights = ZAR__ due to Arabella\n Hotel and Spa", bg="white")
line3 = Label(window, text="Credit Card will be charged on receipt of this form and details will also be used to settle all incidentals not settle on\n departure. A copy of the final folio will be sent to you should there be any unsettled charges.", bg="white")
line4 = Label(window, text="In order to qualify for the above rates, your booking needs to be made on or before 15th January 2016", bg="white")
line5 = Label(window, text="Terms and conditions can be found on the next page.", bg="white")   
line6 = Label(window, text="The rate is valid for seven days before and after the conference dates. Check in time is 14:00 & check out time is 11:00", bg="white")
line7 = Label(window, text="By your signature hereto, you are accepting all terms and conditions specified on this form and confirm that all information\n given is current and accurate.", bg="white")

line1.grid(row=20, column=0,columnspan=4)
line2.grid(row=21, column=0,columnspan=4)
line3.grid(row=22, column=0,columnspan=4)
line4.grid(row=23, column=0,columnspan=4)
line5.grid(row=24, column=0,columnspan=4)
line6.grid(row=25, column=0,columnspan=4)
line7.grid(row=26, column=0,columnspan=4)

p1 = Label(window ,text = "Signature :  ").grid(row = 27,column = 0,sticky = "NSEW")
p1 = Label(window ,text = "Print Name: ").grid(row = 27,column = 2,sticky = "NSEW")
p1 = Label(window ,text = "Date :  ").grid(row = 28,column = 0,sticky = "NSEW")

a1 = Entry(window)
a1.grid(row = 0,column = 1)
b1 = Entry(window)
b1.grid(row = 1,column = 1)
c1 = Entry(window)
c1.grid(row = 2,column = 1)
d1 = Entry(window)
d1.grid(row = 3,column = 1)
e1 = Entry(window)
e1.grid(row = 4,column = 1)
f1 = Entry(window)
f1.grid(row = 5,column = 1)
g1 = Entry(window)
g1.grid(row = 6,column = 1)
h1 = Entry(window)
h1.grid(row = 7,column = 1)
i1 = Entry(window)
i1.grid(row = 8,column = 1)
j1 = Entry(window)
j1.grid(row = 9,column = 1)
k1 = Entry(window)
k1.grid(row = 10,column = 1)
l1 = Entry(window)
l1.grid(row = 11,column = 1)
m1 = Entry(window)
m1.grid(row = 12,column = 1)
p101 = Entry(window)
p101.grid(row = 27,column = 1,sticky = "NSEW")
p102 = Entry(window)
p102.grid(row = 27,column = 3,sticky = "NSEW")
p103 = Entry(window)
p103.grid(row = 28,column = 1,sticky = "NSEW")

btn = Button(window ,text="SUBMIT",command = database,width=20).grid(row=30,column=2)
btn = Button(window,text="DISPLAY RECORD(s)",command=display,width=20).grid(row=30,column=3) 
window.mainloop()

import sqlite3
my_conn = sqlite3.connect('hotel.db')

import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1300x250") 

r_set=my_conn.execute('''SELECT * from HOTEL ''');
i=0 # row value inside the loop 
for HOTEL in r_set: 
    for j in range(len(HOTEL)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, HOTEL[j])
    i=i+1
my_w.mainloop()