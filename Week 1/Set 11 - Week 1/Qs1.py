# 1: Write a python program using structured programming paradigms for displaying
# first name, last name, email, user id, password and confirm password of the user for school
# applications. All the inputs are to read from user at run time and proper conversion also to be
# included in the code. After validating the user name and password display the authorized
# user details in console window.

import getpass, stdiomask
name = input("Enter your name: ")
email = input("Enter your email ID: ")
userid = input("Enter userID: ")
password = stdiomask.getpass("Enter your password: ")

c_p = stdiomask.getpass("Confirm your password: ")
if password == c_p:
    print("Record Entered!")
    print("The name of the student: ",name)
    print("The email ID of the student: ",email)
    print("The user ID of the student: ",userid)
else:
    print("Passwords don't match, try again")