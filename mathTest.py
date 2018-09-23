#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 17, 2018

import random
#This program is a basic math test that uses the random function to create different problems

#Defining our main function
def main():
    #Here we declare our variables
    counter = 0
    studentName = ""
    averageRight = 0.0
    right = 0
    number1 = 0
    number2 = 0
    answer = 0.0

    studentName = inputNames(studentName)


    #A loop to run the program again
    while counter < 10:
        number1, number2 = getNumber()
        answer = getAnswer(number1, number2, answer)
        right = checkAnswer(number1, number2, answer, right)
        counter = counter + 1

    averageRight = results(right, averageRight)
    displayInfo(right, averageRight, studentName)


def inputNames(studentName):
    studentName = input("Enter Student Name:")
    return studentName

def getNumber():
    number1 = random.randint(1,500)
    number2 = random.randint(1,500)
    return number1, number2

def getAnswer(number1, number2, answer):
    print("What is the answer to the following equation")
    print(number1)
    print("+")
    print(number2)
    answer = eval(input("What is the sum:"))
    return answer

def checkAnswer(number1, number2, answer, right):
    if answer == number1 + number2:
        print("Right")
        right = right + 1
    else:
        print("Wrong")
    return right

def results(right, averageRight):
    averageRight = right / 10
    return averageRight

def displayInfo(right, averageRight, studentName):
    print("Information for student:", studentName)
    print("The number right:", right)
    print("The average right is:",averageRight)

main()
    
    
