#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 4,2018


#This is a program to simulate a menu that allows you to order items on the menu
#and displays the total of the price. The program allows you to make as many selections
#as you'd like in one order.


#Call our main Module
def main():
    
    #This is to initialize the variables at the start of the program
    endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount = declareVariables()

    #We call our variables that are defined later in a function
    declareVariables()

    #This is our first loop, as long as the user enters no the order will continue
    while endProgram == 'no':

        #A call to our variable reset function, followed by another while loop same concept as before but this one keeps the order going
        totalBurger, totalSoda, totalFry, total, tax, subtotal = resetVariables()
        while endOrder == 'no':
             print("Enter 1 for Yum Yum Burger")
             print("Enter 2 for Grease Yum Fries")
             print("Enter 3 for Soda Yum")
                
             option = eval(input("Please make your selection here: "))

             #These are our options for the menu, once a selection is made it asks how many of each item the user would like
             if option == 1:
                    totalBurger = getBurger(totalBurger, burgerCount)
             elif option == 2:
                    totalFry = getFry(totalFry, fryCount)
             elif option == 3:
                    totalSoda = getSoda(totalSoda, sodaCount)


             endOrder = input("Do you want to end your order?(Enter no to add more items): ")

        total = calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax)
        printReceipt(total)

        endProgram = input("Do you want to end the program?(Enter no to process a new order): ")
        if endProgram == 'no': #I learned this little trick from Elio, this allows the program to return back to the start if the user enter's no
            main()
        else: #This one I figured out when i typed yes at the end of my program and it just looped the same text, it breaks out of the loop and ends the program
            break

#Below are the functions of the program
def declareVariables():

    endProgram = 'no'
    endOrder = 'no'
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    total = 0
    tax = 0
    subtotal = 0
    option = 0
    burgerCount = 0
    fryCount = 0
    sodaCount = 0
    return (endProgram, endOrder, totalBurger,totalFry, totalSoda, total, tax, subtotal,
            option, burgerCount, fryCount, sodaCount)

def resetVariables():
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    total = 0
    tax = 0
    subtotal = 0
    return totalBurger, totalFry, totalSoda, total, tax, subtotal

def getBurger(totalBurger, burgerCount):
    burgerCount = eval(input("Enter the number of burgers you want: "))
    totalBurger = totalBurger+burgerCount*.99
    return totalBurger

def getFry(totalFry, fryCount):
    fryCount = eval(input("Enter the number of fries you want: "))
    totalFry = totalFry + fryCount * .79
    return totalFry

def getSoda(totalSoda, sodaCount):
    sodaCount = eval(input("Enter the number of soda's you want: "))
    totalSoda = totalSoda + sodaCount * 1.09
    return totalSoda

def calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * .06
    total = subtotal + tax
    return total

def printReceipt(total):
    print("Your total is $", total)
            
main()
