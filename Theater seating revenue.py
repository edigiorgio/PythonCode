#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 23, 2018

#This program will ask for the amount of tickets sold between section A,B, and C of the
#Dramatic Theater. If the input is not valid the program will not accept it and will ask
#for the correct numbers. The program will then display the total income for the even chosen

import sys

#Declaring our global constants
ticketA = 20
ticketB = 15
ticketC = 10

#Defining our main module

def main():

    #Our Priming read to initialize the program
    continueProgram = "yes"

    while continueProgram == "yes":
        #our variables for our program
        seatA = 0
        seatB = 0
        seatC = 0
        total = 0.0
        number = 0

        #Calling our functions
        print("How many seats in section A?")
        seatA = getInput(seatA, seatB, seatC, number)
        print("How many seats in section B?")
        seatB = getInput(seatA, seatB, seatC, number)
        print("How many seats in section C?")
        seatC = getInput(seatA, seatB, seatC, number)
        total = calcTotal(seatA, seatB, seatC)
        displayTotals(total, seatA, seatB, seatC)

        continueProgram = str(input("Do you have another event you would like to check the income on?"))
        #This makes sure the input is valid for the above question
        while continueProgram != "yes" and continueProgram != "no":
            continueProgram = str(input("I'm sorry I didn't understand your answer, please try again:"))
            if continueProgram == "no":
                sys.exit()
            if continueProgram == "yes":
                main()

def getInput(seatA, seatB, seatC, number):
    if number == seatA:
        seatA = int(input("Please enter the number of seats sold:"))
        while seatA < 0 or seatA > 300:
            seatA = int(input("That number of seats is not recognized please enter a valid number:"))
        return seatA
    if number == seatB:
        seatB = int(input("Please enter the number of seats sold:"))
        while seatB < 0 or seatB > 500:
            seatB = int(input("That number of seats is not recognized please enter a valid number:"))
        return seatB
    if number == seatC:
        seatC = int(input("Please enter the number of seats sold:"))
        while seatC < 0 or seatC > 200:
            seatC = int(input("That number of seats is not recognized please enter a valid number:"))
        return seatC

def calcTotal(seatA, seatB, seatC):
    total = (seatA * ticketA) + (seatB * ticketB) + (seatC * ticketC)
    return total

def displayTotals(total, seatA, seatB, seatC):
    print("Your sales for section A were:", (seatA * ticketA))
    print("Your sales for section B were:", (seatB * ticketB))
    print("Your sales for section C were:", (seatC * ticketC))
    print("Your total revenue was %.02f" %total)

main()

