#mysecondprogram.py
#January 18,2018
#Eric DiGiorgio
#This program demonstrates both input and output

def main():
    #Declare and initialize variables (give starting values)
    #int called student_ID
    student_ID = 0
    #int called GPA
    GPA = 0
    #int called Classnumber
    Classnumber = 0

    #Introduction
    print ("WELCOME TO MY PROGRAM!!\n") #\n is a shortcut to skip a line of output

    #Prompt the user for student ID
    #We can assign the variable student_ID a new value of whatever the user types in all in one step like this
    student_ID = input("Enter your Student ID: ") #I found this wont work with the eval function (when entering just numbers)
    #my assumption is it wouldn't work with the eval function because of the length so it registered as a string rather than a value

    #Prompt for GPA
    #When prompting for a numeric value, you must surround your input statement
    #with an eval function. the eval will allow Python to evaluate the input as a numeric value
    GPA = eval(input("Enter your GPA: "))

    #Prompt the user for Class Number
    Classnumber = input("Enter your class number here: ") 

    #Display the user's info on the screen
    #the \n moves to a new line, then the number we typed Student ID: appears, then the \t is a tab.
    #All of this is in the " " so it will print to the screen
    #Then we have a comma to seperate what we are typing from the value of the variable that will be printed

    print("Student ID:\t", student_ID) #\t is a shortcut to tab
    print("GPA:\t", GPA)
    print("Class number:\t", Classnumber)
