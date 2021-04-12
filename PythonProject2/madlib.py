# we are using string for this and we want users to enter a series of inputs that will be considered as a Mad Lib.

user = input("enter your name please..\n")
subject=input("enter your favorouite subject..")
message=input("any message?")

madlib=f"Hi {user}!. Nice to have you welcome to Amisha Madlibs.\nyour desirable subject is {subject} . Want to add any note/message? message added {message}.Thank you for using madlibs."

print(madlib)