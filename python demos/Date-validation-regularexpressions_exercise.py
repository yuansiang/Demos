import datetime
import re

#prompt for nric
# get nric
valid_nric = False
while not valid_nric:
    nric = input("Enter your NRIC: ")
     
    # ^ - starts with, {n} exactly n times, $ - ends with
    nricpattern = re.compile("^[sS][0-9]{7}[a-zA-Z]$")

    if not nricpattern.match(nric):
        print("Invalid NRIC. Enter again.")
    else:
        print("ok")
        valid_nric = True
#prompt for name
validname= False

while not validname:
    name = input("Enter name: ")
    if len(name) == 0:
        print("Empty input, try again.")
    elif not name.isalpha():
        print("Name can only contain alphabets. Try again.")
    elif len(name) >30:
        print("Name can only contain 30 characters at most.")
    else:
        print("ok")
        validname = True
#prompt for class
valid_class = False
while not valid_class:
    class2013 = input("Enter your current class: ")
    classpattern = re.compile("^[1][3][yY][0-6]{1}[Cc][1-8]{2}$")
    if not classpattern.match(class2013):
        print("Invalid Class. Enter again.")
    else:
        print("ok")
        valid_class = True

#prompt for gender
# get gender
valid_gender = False
while not valid_gender:
    gender = input("Enter your gender: ")
    # accept upper and lowercase letters m & f
    pattern = re.compile("[mMfF]")

    if not pattern.match(gender):
        print("Invalid gender")
    else:
        print("ok")
        valid_gender = True
        
