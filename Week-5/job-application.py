import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from tkinter import ttk
import sqlite3
# Create
conn = sqlite3.connect('jobs.db')

# Cursor
c = conn.cursor()

# # Create table
c.execute("""
CREATE TABLE jobs(
  first_name text,
  last_name text,
  email text,
  education text,
  address1 text,
  address2 text,
  country text,
  city text,
  state text,
  zipcode text,
  phone1 text,
  phone2 text,
  hobbies text,
  company text,
  job text,
  duration text,
  r1_name text,
  r1_phone text,
  r2_name text,
  r2_phone text
)
""")


def submit():

  # DB

  # Create
  conn = sqlite3.connect('jobs.db')

  # Cursor
  c = conn.cursor()

  # Insert
  c.execute('INSERT INTO jobs VALUES(:first_name,:last_name,:email,:education,:address1,:address2,:country,:city,:state,:zipcode,:phone1,:phone2,:hobbies,:company,:job,:duration,:r1_name,:r1_phone, :r2_name,:r2_phone)',
  {
    'first_name': first_name.get(),
    'last_name': last_name.get(),
    'email': email.get(),
    'education': education.get(),
    'address1': address1.get(),
    'address2': address2.get(),
    'country': country.get(),
    'city': city.get(),
    'state': state.get(),
    'zipcode': zipcode.get(),
    'phone1': phone1.get(),
    'phone2': phone2.get(),
    'hobbies': hobbies.get(),
    'company': company.get(),
    'job': job.get(),
    'duration': duration.get(), 
    'r1_name': r1_name.get(),
    'r1_phone': r1_phone.get(),
    'r2_name': r2_name.get(),
    'r2_phone': r2_phone.get()}
  )

  # Commit changes
  conn.commit()

  # Close connection
  conn.close()




def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)    

root = tk.Tk()
root.geometry('500x500')
root.title("Job application")

ttk.Label(root, text = "Job Application",font = ("bold", 40)).grid(row = 0,column=0,columnspan=3,pady=2) 
ttk.Label(root, text = "Personal Information",foreground="brown",font = ("bold", 20)).grid(row = 1,column=0,pady=2,sticky=W) 
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 2,column=0,pady=2,sticky=W) 
ttk.Label(root, text = "Email",font = ("bold", 10)).grid(row = 3,column=0,pady=2,sticky=W) 
ttk.Label(root, text = "Education",font = ("bold", 10)).grid(row = 4,column=0,pady=2,sticky=W) 
ttk.Label(root, text = "Resume",font = ("bold", 10)).grid(row = 5,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Address",font = ("bold", 10)).grid(row = 6,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone Number",font = ("bold", 10)).grid(row = 10,column=0,pady=2,sticky=W)
ttk.Label(root, text = "What are your hobbies?",font = ("bold", 10)).grid(row = 11,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Previous/Current Employment details",foreground="brown",font = ("bold", 20)).grid(row = 13,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Company Name",font = ("bold", 10)).grid(row = 14,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Job Title",font = ("bold", 10)).grid(row = 15,column=0,pady=2,sticky=W)
ttk.Label(root, text = "How long were you here?",font = ("bold", 10)).grid(row = 16,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Reference #1",foreground="brown",font = ("bold", 10)).grid(row = 17,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 18,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone",font = ("bold", 10)).grid(row = 19,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Reference #2",foreground="brown",font = ("bold", 10)).grid(row = 20,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 21,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone",font = ("bold", 10)).grid(row = 22,column=0,pady=2,sticky=W)
first_name=tk.Entry(root,width=30) # first name
first_name.insert(0,'First name')
last_name=tk.Entry(root,width=30) # last name
last_name.insert(0,'Last name')
email=tk.Entry(root,width=60) # email
email.insert(0,'user@example.com')
address1=tk.Entry(root,width=60) #address1
address2=tk.Entry(root,width=60) #address2
city=tk.Entry(root,width=20) #city
state=tk.Entry(root,width=20) #state
zipcode=tk.Entry(root,width=20) #zipcode
phone1=tk.Entry(root,width=30)
phone2=tk.Entry(root,width=30)# phone
hobbies=tk.Entry(root,width=180) #hobbies
company=tk.Entry(root,width=30)
job=tk.Entry(root,width=30)
duration=tk.Entry(root,width=30)
r1_name=tk.Entry(root,width=30)
r1_phone=tk.Entry(root,width=30)
r2_name=tk.Entry(root,width=30)
r2_phone=tk.Entry(root,width=30)
first_name.grid(row=2,column=1,pady=2,sticky=W)
last_name.grid(row=2,column=2,pady=2,sticky=W)
email.grid(row=3,column=1,columnspan=2,pady=2,sticky=W)
address1.grid(row=6,column=1,columnspan=2,pady=2,sticky=W)
address2.grid(row=7,column=1,columnspan=2,pady=2,sticky=W)
city.grid(row=9,column=1,pady=2,sticky=W)
state.grid(row=9,column=2,pady=2,sticky=W)
zipcode.grid(row=9,column=3,pady=2,sticky=W)
phone1.grid(row=10,column=1,pady=2,sticky=W)
phone2.grid(row=10,column=2,pady=2,sticky=W)
hobbies.grid(row=12,column=0,columnspan=4,pady=2,sticky=W)
company.grid(row=14,column=1,pady=2,sticky=W)
job.grid(row=15,column=1,pady=2,sticky=W)
duration.grid(row=16,column=1,pady=2,sticky=W)
r1_name.grid(row=18,column=1,pady=2,sticky=W)
r1_phone.grid(row=19,column=1,pady=2,sticky=W)
r2_name.grid(row=21,column=1,pady=2,sticky=W)
r2_phone.grid(row=22,column=1,pady=2,sticky=W)

education = tk.StringVar() 
education.set('Please choose')
choose=ttk.Combobox(root,width=57,textvariable=education)
choose['values']=('12th pass','B.Tech','M.Tech','BS','MS','PhD')
choose.grid(row=4,column=1,columnspan=2,sticky=W)
choose.current()

country = tk.StringVar() 
country.set('Select a Country')
choose=ttk.Combobox(root,width=57,textvariable=country)
choose['values']=('America','Russia','Germany','India','Indonesia','China','Japan')
choose.grid(row=8,column=1,columnspan=2,sticky=W)
choose.current()

btn = Button(root,width=57, text ='Choose file', command = browsefunc) 
btn.grid(row=5,column=1,columnspan=2,sticky=W) 
pathlabel=Label(root)
pathlabel.grid(row=5,column=1,columnspan=2,sticky=W)

Button(root, text='Apply',width=20, command=submit).place(x=180,y=640)
root.mainloop()