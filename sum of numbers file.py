#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 10, 2018

import sys
numbersList = [] #open ended array to accept as much data as the user wants

def sumOfNumbers(): #a simple function to add the numbers in the number list together
    sums = sum(numbersList)
    print("Your totals have been figured, below are the results")
    print(sums)

def writeNumbers(numbers): #This wasn't necessary for what the program asked for but i wanted the practice
    numbersFile = open('numbers.txt','w')  
    for x in range(int(numbers)): 
        numbersFile.write(str(numbersList[x]) + '\n')
    numbersFile.close()

def readNumbers(numbers): #This was all the program asked for but it seemed pointless to design a program that just worked with a specific set of numbers
    numbersFile = open('numbers.txt', 'r')
    print("Just to be clear the numbers you entered are below:")
    for x in range(int(numbers)):
        numbers = numbersFile.readline()
        numbers = numbers.rstrip('\n')     
        print(numbers)
    numbersFile.close() 
    

def main():
    print("Welcome to my one world renowned adding machine")
    print("This program will take any amount of numbers you want to enter and add them all together and display the results for you")
    print("The instructions are simple, the first prompt will ask you how many different numbers you want to add")
    print("The following prompts will ask you for the different numbers you want to add")
    print("When you reach the end of the list it will redisplay your numbers followed by the sum of the numbers")
    print("=======================END OF MESSAGE====================")
    counter = 0 
    endProgram = "no"
    while endProgram == "no":
        while True:
            try:
                numbers = input("How many numbers do you want to enter today:")
                for x in range(int(numbers)):
                    data = input("Enter number " + str(counter + 1) +  " now:")
                    numbersList.append(int(data)) #appends the data into my list
                    counter += 1
                    continue
            except ValueError:
                print("oops something went wrong, try again")
                continue
            writeNumbers(numbers)
            readNumbers(numbers)
            sumOfNumbers()
            
            endProgram = input("Do you want to end the program? ")
            while endProgram != 'yes' or endProgram != 'no':
                if endProgram == 'no':
                    del numbersList[:] #So we start with a fresh list each time
                    main()
                elif endProgram == 'yes':
                    sys.exit()
                else:
                    endProgram = input("I'm confused, did you want to exit or not:")
main()
