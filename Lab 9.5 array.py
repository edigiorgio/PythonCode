#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 26, 2018

#This program calculates the savings on your energy bills spanning over 2 years
#The main function
def main():
    #Our priming read to get the machine going
    endProgram = "no"
    #Our while loop to keep the program going
    while endProgram.lower() == "no":
        notGreenCost = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]#Initialize our arrays(aka lists)
        goneGreenCost = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        savings = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
        
        #Call our functions
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings, months)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
        #Ask if we want to run the program again
        endProgram = input("Do you want to end the program? Yes or No")
#Our functions
def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < len(months):#This runs our functions until it reaches the end of the list for months
        notGreenCost[counter] = float(input("Enter NOT GREEN energy costs for " + str(months[counter]) + ":"))#This is asking the user for input
        counter += 1
    return notGreenCost

def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < len(months):
        goneGreenCost[counter] = float(input("Enter GONE GREEN costs for " + str(months[counter]) + ":"))
        counter += 1
    return goneGreenCost

def energySaved(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < len(months):
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter += 1
    return savings

def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < len(months):
        print("Information for " + months[counter])
        print("Savings $" + str(savings[counter]))
        print("Not Green Costs $" + str(notGreenCost[counter]))
        print("Gone Green Costs $" + str(goneGreenCost[counter]))
        counter += 1

main()
