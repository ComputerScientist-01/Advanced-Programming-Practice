from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as sql

db = sql.connect(host ="localhost",
				user = "root",
    			password = "root",
 				db ="registrationformdb")
cursor = db.cursor()
global window
global window2
global window3
global window4
global window5
root = Tk()
root.title("User Authentication")
root.geometry("400x150")
user_name_var=tk.StringVar()
pass_var=tk.StringVar()
f_name_var=tk.StringVar()
l_name_var=tk.StringVar()
age_var=tk.StringVar()
user_name_var_signup=tk.StringVar()
pass_var_signup=tk.StringVar()
gender_var = tk.StringVar()
full_name_var = tk.StringVar()
email_var = tk.StringVar()

def quit():
    root.quit()

def users_registered():
    window4.destroy()
    global window5
    window5 = Tk()
    window5.title("Submitted")
    window5.geometry("600x200")
    L16 = Label(window5,text="Following users have recently been registered!",font="Helvetica 18 bold",bg="black",fg="white").place(relx=0.5, rely=0.05, anchor=CENTER)
    L17 = Label(window5,text="USERNAME").grid(row=0,column=0,pady=(60,0))
    L17 = Label(window5,text="FIRSTNAME").grid(row=0,column=1,pady=(60,0))
    L17 = Label(window5,text="LASTNAME").grid(row=0,column=2,pady=(60,0))
    L17 = Label(window5,text="AGE").grid(row=0,column=3,pady=(60,0))
    L17 = Label(window5,text="GENDER").grid(row=0,column=4,pady=(60,0))
    L17 = Label(window5,text="EMAIL").grid(row=0,column=5,pady=(60,0))
    L17 = Label(window5,text="FULLNAME").grid(row=0,column=6,pady=(60,0))
    cursor.execute("SELECT * FROM user_details")
    i=1 
    for users in cursor: 
        for j in range(len(users)):
            if(j==5):     
                j+=1
            elif(j>=6):
                E11 = Entry(window5, width=25, fg='black') 
                E11.grid(row=i, column=j-1)
                E11.insert(END, users[j])
            else:
                E11 = Entry(window5, width=25, fg='black') 
                E11.grid(row=i, column=j)
                E11.insert(END, users[j])
        i=i+1
    button_8 = Button(window5,text="QUIT",width=10,command=lambda: quit()).place(relx=0.5,rely=0.84,anchor=CENTER)


def finish(E8=None,E9=None,E10=None,gender_var_form=None,username_var=None):
    global window4
    window4 = Tk()
    window4.title("Submitted")
    window4.geometry("600x200")
    full_name_var = E8.get()
    email_var = E9.get()
    age_var = E10.get()
    try:
        query3= ("""UPDATE user_details SET fullname = %(fullname)s, gender = %(gender)s, age = %(age)s, email = %(email)s WHERE username = %(username)s;""")
        data2 = {
            'fullname': full_name_var,
            'gender': gender_var_form.get(),
            'age': age_var,
            'email': email_var,
            'username':username_var,
            }
        cursor.execute(query3,data2)
        db.commit()
    except sql.Error as e:
        db.rollback()
        print('Error:', e)
    window3.destroy()
    L10 = Label(window4,text="Form has been Submitted Successfully!!",font="Helvetica 18 bold",bg="black",fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
    button_6 = Button(window4,text="QUIT",width=10,command=lambda: quit()).place(relx=0.75,rely=0.90,anchor=CENTER)
    button_7 = Button(window4,text="REGISTERED USERS",width=20,command=lambda: users_registered()).place(relx=0.25,rely=0.90,anchor=CENTER)



def railway_registration(username_var):
    window.destroy()
    global window3
    window3 = Tk()
    window3.title("Railway Registration Form")
    window3.geometry("600x250")
    
    L11 = Label(window3,text="Railway Registration Form",font="Helvetica 18 bold").place(relx=0.5, rely=0.05, anchor=CENTER)
    L12 = Label(window3,text="Full Name: ",font="Helvetica 12").grid(pady=(80,0),row=0,column=0)
    L15 = Label(window3, text="Login Successfully!... Welcome {} ".format(username_var), fg="green", font="bold").place(relx=0.5, rely=0.2, anchor=CENTER)
    E8 = Entry(window3,width=40)
    E8.grid(pady=(80,0),row=0,column=1)
    L13 = Label(window3,text="Email Id: ",font="Helvetica 12").grid(row=1,column=0)
    E9 = Entry(window3,width=40)
    E9.grid(row=1,column=1)
    Label(window3,text="Gender: ", font="Helvetica 12").grid(row=2,column=0)
    gender_var_form = tk.StringVar(value="Please Choose") 
    gender_chosen_form = ttk.Combobox(window3,width=37,textvariable=gender_var_form,state="readonly") 
    # Adding combobox drop down list 
    gender_chosen_form['values'] = ('Male', 'Female', 'Other') 
    gender_chosen_form.grid(row=2,column=1) 
    gender_chosen_form.current()
    L14 = Label(window3,text="Age: ",font="Helvetica 12").grid(row=3,column=0)
    E10 = Entry(window3,width=40)
    E10.grid(row=3,column=1)
    button_5 = Button(window3,text="SUBMIT",width=10,command=lambda: finish(E8,E9,E10,gender_var_form,username_var)).place(relx=0.5,rely=0.84,anchor=CENTER)


def user_signup():
    window.destroy()
    global window2
    window2 = Tk()
    window2.title("Railway Registration-SIGNUP")
    window2.geometry("600x250")
    L4 = Label(window2,text="SIGNUP",font="Helvetica 18 bold").place(relx=0.5, rely=0.09, anchor=CENTER)
    L5 = Label(window2,text="Username: ",font="Helvetica 12").grid(pady=(40,10),row=0,column=0)
    E3 = Entry(window2,width=40)
    E3.grid(pady=(40,10),row=0,column=1)
    L6 = Label(window2,text="Password: ",font="Helvetica 12").grid(row=1,column=0)
    E4 = Entry(window2,width=40,show="*")
    E4.grid(row=1,column=1)
    L7 = Label(window2,text="First Name: ",font="Helvetica 12").grid(row=2,column=0)
    E5 = Entry(window2,width=40)
    E5.grid(row=2,column=1)
    L8 = Label(window2,text="Last Name: ",font="Helvetica 12").grid(row=3,column=0)
    E6 = Entry(window2,width=40)
    E6.grid(row=3,column=1)
    L9 = Label(window2,text="Age: ",font="Helvetica 12").grid(row=4,column=0)
    E7 = Entry(window2,width=40)
    E7.grid(row=4,column=1)
    Label(window2,text="Gender: ", font="Helvetica 12").grid(row=5,column=0)
    gender_var = tk.StringVar(value="Please Choose") 
    gender_chosen = ttk.Combobox(window2,width=37,textvariable=gender_var,state="readonly") 
    # Adding combobox drop down list 
    gender_chosen['values'] = ('Male', 'Female', 'Other') 
    gender_chosen.grid(row=5,column=1) 
    gender_chosen.current()
    button_4 = Button(window2,text="SIGNUP",width=10,command=lambda: window_block(E3,E4,E5,E6,E7,gender_var)).place(relx=0.5,rely=0.90,anchor=CENTER)

def user_login(E1=None,E2=None):
    user_name_var = E1.get()
    pass_var = E2.get()
    query2 = "SELECT * FROM user_details WHERE username = %s AND psswd = %s"
    cursor.execute(query2,[(user_name_var),(pass_var)])
    results = cursor.fetchall()
    if results:
        for i in results:
            railway_registration(user_name_var)
            break
    else:
        L3 = Label(window,text="Username or Password is incorrect, Try Again!",font="Helvetica 12",fg="red").place(relx=0.5, rely=0.75, anchor=CENTER)
       

def window_block(E3=None,E4=None,E5=None,E6=None,E7=None,gender_var=None):
    try:  
        root.destroy()
    except: 
        user_name_var_signup = E3.get()
        pass_var_signup = E4.get()
        f_name_var = E5.get()
        l_name_var = E6.get()
        age_var = E7.get()
        gender_var.get()
        try:
            query = ("INSERT INTO user_details (username,firstname,lastname,age,gender,psswd) VALUES (%(username)s,%(firstname)s,%(lastname)s,%(age)s,%(gender)s,%(psswd)s);")
            data = {
                'username': user_name_var_signup,
                'firstname': f_name_var,
                'lastname': l_name_var,
                'age': age_var,
                'gender': gender_var.get(),
                'psswd': pass_var_signup,
                }
            cursor.execute(query,data)
            db.commit()
        except sql.Error as e:
            db.rollback()
            print('Error:', e)
        window2.destroy()
    global window
    window = Tk()
    window.title("User Authentication")
    window.geometry("400x150")
    L1 = Label(window,text="Login",font="Helvetica 18 bold").place(relx=0.5, rely=0.09, anchor=CENTER)
    L2 = Label(window,text="Username: ",font="Helvetica 12").grid(pady=(40,10),row=0,column=0)
    E1 = Entry(window,width=40)
    E1.grid(pady=(40,10),row=0,column=1)
    L3 = Label(window,text="Password: ",font="Helvetica 12").grid(row=1,column=0)
    E2 = Entry(window,width=40,show="*")
    E2.grid(row=1,column=1)
    button_2 = Button(window,text="LOGIN",width=10,command=lambda: user_login(E1,E2)).place(relx=0.75,rely=0.90,anchor=CENTER)
    button_3 = Button(window,text="SIGNUP",width=10,command=lambda: user_signup()).place(relx=0.25,rely=0.90,anchor=CENTER)

button_1 = Button(root,text="Click here!",width=10,command=lambda: window_block()).place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()