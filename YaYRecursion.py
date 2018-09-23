#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 27, 2018

import sys
from time import sleep

sys.setrecursionlimit(100000000)#This is to raise the base recursion limit too 100,000,000 it does nothing except cause IDLE to crash and restart. thought it was interesting so i left it

#this program takes input and then calls a function recursively to add the numbers
#from 1 all the way to the number used for input
#Also added the ackermann function because it seemed cool and I wanted to see what it did... and it gives the program a little extra besides.

            
def main():#Main module
    
    print("Welcome to my Recursion program")
    print("You have three choices")
    print("A simple addition machine that adds numbers from 1 to your input")
    print("Or the Ackermann Function")
    print("Or the ability to exit of course")
    print("1 to add\n2 for Ackermann\n3 to exit")
    while True:#Statements to only accept integers as input
        try:
            choice = int(input("Please make a selection:"))
        except ValueError:
            choice = int(input("That wasn't a real number, try again:"))
            continue
        else:
            if choice == 1: #My menu, for fun of course
                while True:
                    try:
                        number = int(input('Enter a number for your base and this program will add every number between 1 and your number together and display the results:'))
                    except ValueError:
                        sleep(6)#This is to give some pause in between...
                        print("Only integers please!")
                        print("Returning to the main menu")
                        break
                    else:
                        temp = adderModule(number)
                        print("The results are in and the total is:%s" %temp)
                        sleep(2)
                        main()
            elif choice == 2: #ackermann function... acts funky with different arguments
                while True:
                    try:
                        print("***WARNING ANYTHING OVER 3 and 8 WILL CRASH***")
                        number2 = int(input('give me your First Argument'))
                        number3 = int(input('give me your Second Argument'))
                    except ValueError:
                        sleep(6)#The extended time was my little joke to make it seem like the computer is stuck thinking about input besides an integer
                        print("NUMBERS ONLY")
                        print("Returning to the main menu")
                        break
                    else:
                        duh = ackermann(number2, number3)
                        print(duh)
                        break
            elif choice == 3:
                sys.exit()

def ackermann(m, n):#I dont fully understand this but its what the book says and it seems to work
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
def adderModule(add):
    if add == 0:
        return 0
    else:
        return add + adderModule(add - 1)

    

main()

