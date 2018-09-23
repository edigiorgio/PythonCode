#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 18, 2018

#This program will generate 100 random numbers and test each number to see
#if it is even or odd, then this program will record the results and display
#them at the end of the program

import random

def main():
    #We initialize our variables
    counter = 0
    number = 0
    name = ""
    even = 0
    odd = 0
    answer = ""
    
    #Calling or first function
    welcomeMessage(name, answer)
    
    #A loop to run or program for 100 iterations
    while counter < 100:
        
        #A function to generate random numbers and determine if there even or odd
        even = numberGenerator(number, even, odd)
        odd = numberGenerator(number, even, odd)
        #A function to keep count of our iterations
        counter = countingMachine(counter)
        
    #a function to display our total even and odd numbers
    total(even, odd)

#This function welcomes the user and explains the program
def welcomeMessage(name, answer):
    print("Welcome to my even and odd machine")
    print("""This program will generate 100 random numbers and then
determine if there even or odd""")
    name = input("Please tell me your name so we can begin: ")
    print("Thank you", name)
    answer = input("are you ready to begin?(type yes or no): ")
    if answer == str("yes") or answer == str("Yes"):
        return answer
    else:
        welcomeMessage(name, answer)

#This function generates the random numbers and determines if there even or odd
def numberGenerator(number, even, odd):
    number = random.randint(1,100)
    print(number)
    #these if and elif statements are the determining factors of even and odd
    if number % 2 == 0:
        print("This number is even")
        even = even + 1
    elif number % 2 != 0:
        print("This number is odd")
        odd = odd + 1   
    return even

def countingMachine(counter):
    counter = counter + 1
    return counter

def total(even, odd):
    print("The total even and odd numbers were")
    print("Even: ", even)
    print("Odd: ", odd)
    print("thats all folks")
        
main()
