import getpass, stdiomask   #asterisks in password
name = input("Enter your name: ")
email = input("Enter your email ID: ")
userid = input("Enter userID: ")
password = stdiomask.getpass("Enter your password: ")

c_p = getpass.getpass("Confirm your password: ")
if password == c_p:
   print("Record Entered!")
   print("The name of the student: ",name)
   print("The email ID of the student: ",email)
   print("The user ID of the student: ",userid)
else:
   print("Passwords don't match, try again")