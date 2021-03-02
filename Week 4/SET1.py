import tkinter as tk
from tkinter.ttk import *
from tkinter.tix import *

window=tk.Tk()
window['background']='#6449C6'
window.geometry('600x800')

window.title("APP")

f1=tk.Label(window, text="FIRST NAME", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=0)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=150, y=12)

maxchar1=tk.Label(window, text="(max 30 characters a-z and A-Z)", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar1.place(x=250, y=12)

l1=tk.Label(window, text="LAST NAME", bg='#6449C6', fg='white', padx=10)
l1.place(x=5, y=50)

l1t=tk.Text(window, height=0.8, width=12)
l1t.place(x=150, y=50)

maxchar2=tk.Label(window, text="(max 30 characters a-z and A-Z)", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar2.place(x=250, y=50)

dob=tk.Label(window, text="DATE OF BIRTH", bg='#6449C6', fg='white', pady=15)
dob.place(x=13, y=75)

monthchosen = Combobox(window, width = 7) 
daychosen = Combobox(window, width = 7) 
yearchosen = Combobox(window, width = 7) 


dayl=[]
for i in range(0 ,32):
    dayl.append(str(i))
dayl[0]='Day:'
daychosen['values'] = dayl

yearl=[]
for i in range(1968 ,2022):
    yearl.append(str(i))
yearl[0]='Year:'
yearchosen['values'] = yearl
  
monthchosen['values'] = ('Month:',
                          ' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
  
daychosen.current(0) 
daychosen.place(x=150, y=88)

monthchosen.current(0) 
monthchosen.place(x=220, y=88)

yearchosen.current(0)
yearchosen.place(x=290, y=88)

e1=tk.Label(window, text="EMAIL ID", bg='#6449C6', fg='white', padx=10)
e1.place(x=5, y=125)

e1t=tk.Text(window, height=0.8, width=12)
e1t.place(x=150, y=125)

l1=tk.Label(window, text="MOBILE NUMBER", bg='#6449C6', fg='white', padx=10, pady=10)
l1.place(x=5, y=150)

l1t=tk.Text(window, height=0.8, width=18)
l1t.place(x=150, y=160)

maxchar3=tk.Label(window, text="(10 digit number)", bg='#6449C6', fg='white', font=("Arial", 8), padx = -100)
maxchar3.place(x=250, y=160)

l1=tk.Label(window, text="GENDER", bg='#6449C6', fg='white', padx=10, pady=10)
l1.place(x=5, y=190)

maxchar3=tk.Label(window, text="Male", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=150, y=200)

tk.Radiobutton(window,value=1, bg='#6449C6').place(x=185,y=200)

maxchar3=tk.Label(window, text="Female", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=225, y=200)

tk.Radiobutton(window,value=2, bg='#6449C6').place(x=270,y=200)

l1=tk.Label(window, text="ADDRESS", bg='#6449C6', fg='white', padx=10, pady=15)
l1.place(x=5, y=225)

l1t=tk.Text(window, height=4, width=18)
l1t.place(x=150, y=240)

f1=tk.Label(window, text="CITY", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=315)

f1t=tk.Text(window, height=0.8, width=12)
f1t.place(x=150, y=328)

maxchar1=tk.Label(window, text="(max 30 characters a-z and A-Z)", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar1.place(x=250, y=328)

f1=tk.Label(window, text="PINCODE", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=350)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=150, y=365)

maxchar1=tk.Label(window, text="(6 digit number)", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar1.place(x=250, y=365)

f1=tk.Label(window, text="STATE", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=390)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=150, y=402)

maxchar1=tk.Label(window, text="(max 30 characters a-z and A-Z)", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar1.place(x=250, y=402)

f1=tk.Label(window, text="COUNTRY", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=428)

countrychosen = Combobox(window, width = 7) 
c=["India", "Malaysia", "Japan", "U.S.", "Germany"]
countrychosen['values'] = c
countrychosen.current(0) 
countrychosen.place(x=150, y=440)

f1=tk.Label(window, text="HOBBIES", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=470)

maxchar3=tk.Label(window, text="Drawing", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=150, y=485)

ch1 = tk.Checkbutton(window, bg='#6449C6')
ch1.place(x=195, y=482)

maxchar3=tk.Label(window, text="Singing", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=240, y=485)

ch1 = tk.Checkbutton(window, bg='#6449C6')
ch1.place(x=280, y=482)

maxchar3=tk.Label(window, text="Dancing", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=325, y=485)

ch1 = tk.Checkbutton(window, bg='#6449C6')
ch1.place(x=370, y=482)

maxchar3=tk.Label(window, text="Others", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=150, y=508)

ch1 = tk.Checkbutton(window, bg='#6449C6')
ch1.place(x=195, y=505)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=220, y=508)

f1=tk.Label(window, text="QUALIFICATION", bg='#6449C6', fg='white', padx=10, pady=15)
f1.place(x=5, y=532)

maxchar3=tk.Label(window, text="Sl.No.\tExamination\tBoard\t\tPercentage\tYear of passing", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=150, y=540)

maxchar3=tk.Label(window, text="1\tClass X \n\n 2\t Class XII \n\n   3\t   Graduation\n\n4\tMasters", bg='#6449C6', fg='white', font=("Arial", 8))
maxchar3.place(x=150, y=560)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=270, y=562)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=375, y=562)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=480, y=562)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=270, y=588)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=375, y=588)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=480, y=588)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=270, y=614)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=375, y=614)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=480, y=614)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=270, y=640)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=375, y=640)

f1t=tk.Text(window, height=0.8, width=12 )
f1t.place(x=480, y=640)

b=tk.Button(window, text="Submit", bd = '5')
b.place(x=320, y=665)

b=tk.Button(window, text="Reset", bd = '5')
b.place(x=400, y=665)

window.mainloop()