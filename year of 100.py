import time
import datetime

age = 0


print("Welcome to my program to tell you the year you turn 100 years olds")
age = eval(input("Please enter your age: "))

years2100 = 100 - age
currentDate = datetime.date.today()
yearOf100 = (2018 - age) + 100

print(yearOf100)
