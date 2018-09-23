#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 7, 2018

#System function for later user
import sys
#Globals
notGreenCost = [0.0] * 12
goneGreenCost = [0.0] * 12
savings = [0.0] * 12
months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
#main function
def main():
    #Priming read
    endProgram = "no"
    option = 0
    print("Welcome to the GREEN vs. NOT GREEN savings calculator")
    #Loop to start/run the program
    while endProgram == "no":
        while True: #input validation to only alow numbers
            try:
                option = int(input("""Please make a selection below\n1.)Enter info\n2.)Display info
3.)Write to file\n4.)Read from File\nEnter option:"""))
            except ValueError:#Kicks back anything not a number
                print("This is not an acceptable answer try numbers 1-4:")
                continue
            if option == 1:
                getNotGreen()
                getGoneGreen()
                energySaved()
            elif option == 2:
                displayInfo()
            elif option == 3:
                writeToFile()
            elif option == 4:
                readFromFile()
            else: #kicks back a wrong number
                print("That is not an option")
                main()
            
        endProgram = input("Do you want to end the program? Yes or no: ")
        #Input validation for the end program
        while endProgram != "yes" or endProgram != "no":
            if endProgram == "no":
                main()
            elif endProgram == "yes":
                sys.exit() #ends the program
            else:
                print("Please enter yes or no")
                endProgram = input("Do you want to end the program? yes or no: ")

def writeToFile():
    savingsFile = open('savings1.txt', 'w')#Opens file, i found that using the append feature created issues with the length of the file.
    for x in range(len(months)): #loops my file and data into the file
        savingsFile.write(str(months[x])+ '\n')
        savingsFile.write(str(savings[x])+ '\n')
    savingsFile.close()

def readFromFile():
    savingsFile = open('savings1.txt', 'r')#Opens the file with read only permissions
    for x in range(len(months)):#loops the file
        month = savingsFile.readline()#Reads the months in the file
        month = month.rstrip('\n')#Strips the endline character at the end of my months
        print(month)
        saving = savingsFile.readline()
        saving = saving.rstrip('\n')
        print(saving)
    savingsFile.close()

def getNotGreen():
    for x in range(len(months)):
        notGreenCost[x] = float(input("Enter NOT GREEN energy costs for " + months[x] + ':'))
    
        
def getGoneGreen():
    for x in range(len(months)):
        goneGreenCost[x] = float(input("Enter GONE GREEN energy costs for " +months[x] + ':'))
    return goneGreenCost
    
def energySaved():
    for x in range(len(months)):
        savings[x] = notGreenCost[x] - goneGreenCost[x]
    return savings
    

def displayInfo():
    for x in range(12):
        print("Information for " + months[x])
        print("Savings $" + str(savings[x]))
        print("Not Green Costs $" + str(notGreenCost[x]))
        print("Gone Green Costs $" + str(goneGreenCost[x]))

main()
