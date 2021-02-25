from tkinter import *

root = Tk()
root.title("Week 4 GUI")
root.geometry("850x950")
# root.configure(bg = "#f0b390", foreground="black")

a = Label(root ,text = "MANUAL", font=("Roboto", 25,"underline"), pady = 30).grid(row = 0,column = 1)
a = Label(root ,text = "FORM", font=("Roboto", 25, "underline"), pady = 30).grid(row = 0,column = 2)
b = Label(root ,text = "Full Name").grid(row = 1,column = 0)
c = Label(root ,text = "Email Id").grid(row = 2,column = 0)
d = Label(root ,text = "Contact Number").grid(row = 3,column = 0)

b1 = Entry(root,width=20).grid(row = 1,column = 1)
c1 = Entry(root,width=20).grid(row = 2,column = 1)
d1 = Entry(root,width=20).grid(row = 3,column = 1)

R = Label(root ,text = "Registration", padx= 10,font=("Comic Sans MS", 18, "bold")).grid(row = 1,column = 3)
D = Label(root ,text = "Details",padx= 10, font=("Comic Sans MS", 18, "bold")).grid(row = 2,column = 3)

rp1 = Label(root ,text = "Registration Period", font=("Comic Sans MS", 18, "bold"),padx = 5, pady=30).grid(row = 5,column = 0)
rp1b = Radiobutton(root, text="One year", padx = 20, pady=5).grid(row = 5, column = 1 )
# rp2 = Label(root ,text = "Registration Period").grid(row = 6,column = 0)
rp2b = Radiobutton(root, text="Two Years", padx = 20, pady=5).grid(row = 5, column = 2 )
# rp3 = Label(root ,text = "Registration Period").grid(row = 7,column = 0)
rp3b = Radiobutton(root, text="Three Years", padx = 20, pady=5).grid(row = 5, column = 3 )

# btn = Button(root ,text="Submit").grid(row=7,column=1)

RT = Label(root ,text = "Registration Type", font=("Comic Sans MS", 20, "bold"),padx = 5, pady=10).grid(row = 7,column = 0)

rt1b = Radiobutton(root, text="Original", padx = 20, pady=5).grid(row = 8, column = 0 )
rt2b = Radiobutton(root, text="Private", padx = 20, pady=5).grid(row = 8, column = 1)
rt3b = Radiobutton(root, text="Renewal", padx = 20, pady=5).grid(row = 8, column = 2)
rt4b = Radiobutton(root, text="Re-Issue", padx = 20, pady=5).grid(row = 8, column = 3)
rt5b = Radiobutton(root, text="Rental Vehicle", padx = 20, pady=5).grid(row = 9, column = 0 )
rt6b = Radiobutton(root, text="TLPN", padx = 20, pady=5).grid(row = 9, column = 1)
rt7b = Radiobutton(root, text="For Hire", padx = 20, pady=5).grid(row = 9, column = 2)
rt8b = Radiobutton(root, text="Ridesharing", padx = 20, pady=5).grid(row = 9, column = 3)

OI = Label(root ,text = "Owner Information", font=("Comic Sans MS", 20, "bold"),padx = 5, pady=30).grid(row = 11,column = 0)

oi1 = Label(root ,text = "Owner Full name", pady=5).grid(row = 12,column = 0)
oi2 = Label(root ,text = "Telephone No", pady=5).grid(row = 12,column = 2)
oi3 = Label(root ,text = "Co-Owner Full name", pady=5).grid(row = 18,column = 0)
oi4 = Label(root ,text = "Telephone No", pady=5).grid(row = 18,column = 2)

oib1 = Entry(root,width=20).grid(row = 12,column = 1)
oib2 = Entry(root,width=20).grid(row = 12,column = 3)
oib3 = Entry(root,width=20).grid(row = 18,column = 1)
oib4 = Entry(root,width=20).grid(row = 18,column = 3)

oi5 = Label(root ,text = "Owner Address", pady=5).grid(row = 15,column = 0)
oi6 = Label(root ,text = "State", pady=5).grid(row = 15,column = 2)
oi7 = Label(root ,text = "City", pady=5).grid(row = 16,column = 0)
oi8 = Label(root ,text = "Zip", pady=5).grid(row = 16,column = 2)

oib5 = Entry(root,width=20).grid(row = 15,column = 1)
oib6 = Entry(root,width=20).grid(row = 15,column = 3)
oib7 = Entry(root,width=20).grid(row = 16,column = 1)
oib8 = Entry(root,width=20).grid(row = 16,column = 3)

oi9 = Label(root ,text = "Co-Owner Address", pady=5).grid(row = 20,column = 0)
oi10 = Label(root ,text = "State", pady=5).grid(row = 20,column = 2)
oi11 = Label(root ,text = "City", pady=5).grid(row = 22,column = 0)
oi12 = Label(root ,text = "Zip", pady=5).grid(row = 22,column = 2)

oib5 = Entry(root,width=20).grid(row = 20,column = 1)
oib6 = Entry(root,width=20).grid(row = 20,column = 3)
oib7 = Entry(root,width=20).grid(row = 22,column = 1)
oib8 = Entry(root,width=20).grid(row = 22,column = 3)

AI = Label(root ,text = "Additional Information", pady = 30,padx=5, font=("Comic Sans MS", 20, "bold")).grid(row = 24,column = 0)

ai1 = Label(root ,text = "Location(City/Country/Town)", pady=5).grid(row = 25,column = 0)
aib1 = Entry(root,width=20).grid(row = 25,column = 1)
ai1 = Label(root ,text = "Military Duty/Service - Details", pady=5, padx = 10).grid(row = 25,column = 2)
aib1 = Entry(root,width=20).grid(row = 25,column = 3)

ai2 = Label(root ,text = "Mailing Address", pady=5).grid(row = 27,column = 0)
ai3 = Label(root ,text = "State", pady=5).grid(row = 27,column = 2)
ai4 = Label(root ,text = "City", pady=5).grid(row = 29,column = 0)
ai5 = Label(root ,text = "Zip", pady=5).grid(row = 29,column = 2)

aib2 = Entry(root,width=20).grid(row = 27,column = 1)
aib3 = Entry(root,width=20).grid(row = 27,column = 3)
aib4 = Entry(root,width=20).grid(row = 29,column = 1)
aib5 = Entry(root,width=20).grid(row = 29,column = 3)

root.mainloop() 