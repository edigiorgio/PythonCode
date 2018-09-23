#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 18, 2018

import sys
from time import sleep


#This program will display a menu that has 4 planets listed. Once the user makes a choice
#the program will display information about that planet

print("Welcome to the Astronomy Helper, please make a selection below")
print("==============================================================")
sleep(3)

def main():
    selection = 0
    endProgram = 'no'

    while endProgram == 'no':
        print("Which planet would you like to see data on?")
        print("1.)Mercury")
        print("2.)Venus")
        print("3.)Earth")
        print("4.)Mars")
        print("5.)Exit the program")
        selection = eval(input("Make your selection:"))

        while selection < 1 or selection > 5:
            print("That is not a valid selection")
            selection = input("Please try again:")

        if selection == 1:
            print("You have Chosen Mercury")
            sleep(1)
            print("+++++++++++++++++++++++")
            sleep(1)
            print("Average distance from the sun\t57.9 million kilometers")
            sleep(1)
            print("Mass\t\t\t\t3.31X10^23kg")
            sleep(1)
            print("Surface temperature\t\t-173 to 430 degrees celsius")
            sleep(5)
        elif selection == 2:
            print("You have Chosen Venus")
            print("+++++++++++++++++++++++")
            print("Average distance from the sun\t108.2 million kilometers")
            print("Mass\t\t\t\t4.87X10^24kg")
            print("Surface temperature\t\472 degrees celsius")
            sleep(5)
        elif selection == 3:
            print("You have Chosen Earth")
            print("+++++++++++++++++++++++")
            print("Average distance from the sun\t149.6 million kilometers")
            print("Mass\t\t\t\t5.967X10^23kg")
            print("Surface temperature\t\t-50 to 50 degrees celsius")
            sleep(5)
        elif selection == 4:
            print("You have Chosen Mars")
            print("+++++++++++++++++++++++")
            print("Average distance from the sun\t227.9 million kilometers")
            print("Mass\t\t\t\t0.6424X10^23kg")
            print("Surface temperature\t\t-140 to 20 degrees celsius")
            sleep(5)
        elif selection == 5:
            sys.exit()

        endProgram = input("Would you like to exit the program?")

        while endProgram != 'yes' and endProgram != 'no':
            if endProgram == 'yes':
                sys.exit()
            elif endProgram == 'no':
                main()
            else:
                print('that is not correct, try again')
                endProgram = input("Would you like to exit the program?")

main()
