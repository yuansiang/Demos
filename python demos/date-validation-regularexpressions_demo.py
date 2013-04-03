import datetime
import re
curr_date = datetime.date.today()
print (curr_date.isoformat())
print(curr_date.strftime("%d-%m-%y")) # DD-MM-YY
print(curr_date.strftime("%d-%m-%Y")) # DD-MM-YYYY
print(curr_date.strftime("%y%m%d")) # YYMMDD
print(curr_date.strftime("%Y%m%d")) # YYYYMMDD

d = input("Enter date in DD-MM-YYYY format: ")

try:
    valid_date = datetime.datetime.strptime(d, "%d-%m-%Y")
except ValueError:
    print ("Invalid Date")
    
##valid range for age 1 - 100 
## 
##set boolean valid_age to false
valid_age = False
##loop until valid_age is true
while not valid_age:
##    get age
    age = input("Enter your age: ")
##    if empty input display empty input message and allow re-entry
    if len(age) == 0:
            print("Empty input. Try again.")
##    if not a number display wrong data type and allow re-entry
    elif not age.isdigit():
        print("Age is a number. Try again.")
##    if not within valid range display invalid range and allow re-entry
    elif not 0 < int(age) <= 100:
        print("Are you human. Enter between 1 and 100.")
##    else set valid_age to true 
    else:
        valid_age = True
print(age)

# get gender
gender = input("Enter your gender: ")
# accept upper and lowercase letters m & f
pattern = re.compile("[mMfF]")

if not pattern.match(gender):
    print("Invalid gender")
else:
    print("ok")
