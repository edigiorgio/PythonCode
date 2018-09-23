#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 22, 2018

#this is used later in the code to end the program
import sys


#This program will calculate and display the number of minutes over the contract limit that
#a cell phone user incurred.

#Defining our main module
def main():

    #Declaring local variables
    endProgram = "no"

    #a loop to keep our program going
    if endProgram == "no":
        
        #More variables to run in our loop
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0

        #calling our functions that are defined below
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)
        #This asks the user for input to whether or not they want to continue
        endProgram = input("Do you want to end the program?(Type yes or no):")
        
        
        #A loop for input validation...
        while endProgram != "yes" or endProgram != "no":
            if endProgram == "no":
                main() #a call back to main if they say no
            elif endProgram == "yes":
                sys.exit() #ends the program if they say yes
            else:
                print("Please enter yes or no") #this makes sure only yes or no is entered
                endProgram = input("Do you want to end the program? yes or no: ")
            
            
#A few functions to make our program run
def getAllowed(minutesAllowed):
    minutesAllowed = eval(input("How many minutes are allowed:"))
    while minutesAllowed < 200 or minutesAllowed > 800:
        print("Please enter minutes between 200 and 800")
        minutesAllowed = eval(input("How man minutes are allowed:"))
    return minutesAllowed

def getUsed(minutesUsed):
    minutesUsed = eval(input("How many minutes were used:"))
    while minutesUsed < 0:
        print("Please enter minutes of at least 0")
        minutesUsed = eval(input("How many minutes were used:"))
    return minutesUsed

def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    extra = 0.0
    if minutesUsed <= minutesAllowed:
        totalDue = 74.99
        minutesOver = 0
        print("You were not over your minutes for the month")
    else:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * .20
        totalDue = 74.99 + extra
        print("You were over your minutes by:", minutesOver)
    return totalDue, minutesOver

def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print("-----------MONTHLY USE REPORT----------")
    print("Minutes allowed were:", minutesAllowed)
    print("Minutes used were:", minutesUsed)
    print("Minutes over were:", minutesOver)
    print("Total due is $%0.2f" % totalDue)

main()
