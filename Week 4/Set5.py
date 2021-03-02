from tkinter import *

root=Tk()
root.title("CAR RENTAL RECEIPT")
root.geometry('700x800')

#Labels
g1=Label(root, text="CAR RENTAL RECEIPT", font="Calibri 18 bold")

l1=Label(root, text="Date: ")
e1=Entry(root,width=30, borderwidth=2)
l2=Label(root, text="Receipt #: ")
e2=Entry(root,width=30, borderwidth=2)

l3=Label(root, text="Rental Company Info", font="Calibri 12 bold")
l3_1=Label(root, text="Company: ")
e3_1=Entry(root,width=30, borderwidth=2)
l3_2=Label(root, text="Representative: ")
e3_2=Entry(root,width=30, borderwidth=2)
l3_3=Label(root, text="Location: ")
e3_3=Entry(root,width=30, borderwidth=2)
l3_4=Label(root, text="City/State/ZIP: ")
e3_4=Entry(root,width=30, borderwidth=2)
l3_5=Label(root, text="Phone: ")
e3_5=Entry(root,width=30, borderwidth=2)

l4=Label(root, text="Lessee Info", font="Calibri 12 bold")
l4_1=Label(root, text="License: ")
e4_1=Entry(root,width=30, borderwidth=2)
l4_2=Label(root, text="Representative: ")
e4_2=Entry(root,width=30, borderwidth=2)
l4_3=Label(root, text="Address: ")
e4_3=Entry(root,width=30, borderwidth=2)
l4_4=Label(root, text="City/State/ZIP: ")
e4_4=Entry(root,width=30, borderwidth=2)
l4_5=Label(root, text="Phone: ")
e4_5=Entry(root,width=30, borderwidth=2)

g2=Label(root, text="Vehicle Information", font="Calibri 18 bold")

l5_1=Label(root, text="VIN: ")
e5_1=Entry(root,width=30, borderwidth=2)
l5_2=Label(root, text="Make: ")
e5_2=Entry(root,width=30, borderwidth=2)
l5_3=Label(root, text="Year: ")
e5_3=Entry(root,width=30, borderwidth=2)
l5_4=Label(root, text="Color: ")
e5_4=Entry(root,width=30, borderwidth=2)

l6_1=Label(root, text="Registration: ")
e6_1=Entry(root,width=30, borderwidth=2)
l6_2=Label(root, text="Model: ")
e6_2=Entry(root,width=30, borderwidth=2)
l6_3=Label(root, text="Mileage: ")
e6_3=Entry(root,width=30, borderwidth=2)

h1=Label(root, text="VIN", font="Calibri 12 bold")
h1_1=Entry(root,width=14, borderwidth=2)
h1_2=Entry(root,width=14, borderwidth=2)
h1_3=Entry(root,width=14, borderwidth=2)

h2=Label(root, text="Cost/Day", font="Calibri 12 bold")
h2_1=Entry(root,width=12, borderwidth=2)
h2_2=Entry(root,width=12, borderwidth=2)
h2_3=Entry(root,width=12, borderwidth=2)

h3=Label(root, text="# of Days", font="Calibri 12 bold")
h3_1=Entry(root,width=19, borderwidth=2)
h3_2=Entry(root,width=19, borderwidth=2)
h3_3=Entry(root,width=19, borderwidth=2)

h4=Label(root, text="Additional Costs", font="Calibri 12 bold")
h4_1=Entry(root,width=18, borderwidth=2)
h4_2=Entry(root,width=18, borderwidth=2)
h4_3=Entry(root,width=18, borderwidth=2)

h4l1=Label(root, text="Subtotal: ")
h4l2=Label(root, text="Tax (%): ")
h4l3=Label(root, text="Total: ")
h4l4=Label(root, text="Amount paid: ")

h4e1=Entry(root,width=8, borderwidth=2)
h4e2=Entry(root,width=9, borderwidth=2)
h4e3=Entry(root,width=10, borderwidth=2)
h4e4=Entry(root,width=4, borderwidth=2)

h5=Label(root, text="Line Total", font="Calibri 12 bold")
h5_1=Entry(root,width=16, borderwidth=2)
h5_2=Entry(root,width=16, borderwidth=2)
h5_3=Entry(root,width=16, borderwidth=2)
h5_4=Entry(root,width=16, borderwidth=2)
h5_5=Entry(root,width=16, borderwidth=2)
h5_6=Entry(root,width=16, borderwidth=2)
h5_7=Entry(root,width=16, borderwidth=2)

xl1=Label(root, text="Payment Method: ")
ck1=Checkbutton(root, text='Cash. ', onvalue=1, offvalue=0)
ck2=Checkbutton(root, text='Check No.: ', onvalue=1, offvalue=0)
ent1=Entry(root,width=31, borderwidth=2)
ck3=Checkbutton(root, text='Credit No.: ', onvalue=1, offvalue=0)
ent3=Entry(root,width=41, borderwidth=2)
ck4=Checkbutton(root, text='Other.: ', onvalue=1, offvalue=0)
ent4=Entry(root,width=44, borderwidth=2)

lasl1=Label(root, text="Authorized Signature: ", font="Calibri 10 bold")
lasl2=Label(root, text="Representative Name: ", font="Calibri 10")

lase1=Entry(root,width=22, borderwidth=2)
lase2=Entry(root,width=20, borderwidth=2)


#Positioning
l1.place(x=10, y=45)
e1.place(x=50, y=45)
l2.place(x=10, y=75)
e2.place(x=73, y=75)

l3.place(x=10, y=110)
l3_1.place(x=10, y=150)
l3_2.place(x=10, y=180)
l3_3.place(x=10, y=210)
l3_4.place(x=10, y=240)
l3_5.place(x=10, y=270)

e3_1.place(x=110, y=150)
e3_2.place(x=110, y=180)
e3_3.place(x=110, y=210)
e3_4.place(x=110, y=240)
e3_5.place(x=110, y=270)

l4.place(x=320, y=110)
l4_1.place(x=320, y=150)
l4_2.place(x=320, y=180)
l4_3.place(x=320, y=210)
l4_4.place(x=320, y=240)
l4_5.place(x=320, y=270)

e4_1.place(x=420, y=150)
e4_2.place(x=420, y=180)
e4_3.place(x=420, y=210)
e4_4.place(x=420, y=240)
e4_5.place(x=420, y=270)

g1.place(x=240, y=0)
g2.place(x=240, y=300)

l5_1.place(x=10, y=360)
l5_2.place(x=10, y=390)
l5_3.place(x=10, y=420)
l5_4.place(x=10, y=450)

e5_1.place(x=60, y=360)
e5_2.place(x=60, y=390)
e5_3.place(x=60, y=420)
e5_4.place(x=60, y=450)

l6_1.place(x=320, y=360)
l6_2.place(x=320, y=390)
l6_3.place(x=320, y=420)

e6_1.place(x=420, y=360)
e6_2.place(x=420, y=390)
e6_3.place(x=420, y=420)

h1.place(x=70, y=490)
h2.place(x=160, y=490)
h3.place(x=290, y=490)
h4.place(x=400, y=490)
h5.place(x=560, y=490)

h1_1.place(x=40, y=520)
h1_2.place(x=40, y=545)
h1_3.place(x=40, y=570)

h2_1.place(x=150, y=520)
h2_2.place(x=150, y=545)
h2_3.place(x=150, y=570)

h3_1.place(x=260, y=520)
h3_2.place(x=260, y=545)
h3_3.place(x=260, y=570)

h4_1.place(x=400, y=520)
h4_2.place(x=400, y=545)
h4_3.place(x=400, y=570)
h4l1.place(x=400, y=595)
h4l2.place(x=400, y=620)
h4l3.place(x=400, y=645)
h4l4.place(x=400, y=670)

h4e1.place(x=460, y=595)
h4e2.place(x=454, y=620)
h4e3.place(x=447, y=645)
h4e4.place(x=483, y=670)

h5_1.place(x=540, y=520)
h5_2.place(x=540, y=545)
h5_3.place(x=540, y=570)
h5_4.place(x=540, y=595)
h5_5.place(x=540, y=620)
h5_6.place(x=540, y=645)
h5_7.place(x=540, y=670)

xl1.place(x=40, y=595)
ck1.place(x=40, y=620)
ck2.place(x=100, y=620)
ck3.place(x=40, y=645)
ck4.place(x=40, y=670)

ent1.place(x=188, y=623)
ent3.place(x=128, y=649)
ent4.place(x=110, y=675)

lasl1.place(x=380, y=710)
lasl2.place(x=390, y=735)

lase1.place(x=505, y=710)
lase2.place(x=518, y=735)

root.mainloop()