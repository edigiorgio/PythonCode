#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 3, 2018


#This program will calculate your Body Mass Index based on your input and then decide
#if you are underweight, overweight, or the optimal weight for your height



#To start we define our main module of the program
def main():

    #Now we declare our local variables
    weight = int(input("Please enter your weight: "))
    height = 0
    bodyMassIndex = 0.0

    #Now we call our functions (they will be defined later in the program)
    getWeight(weight)
    getHeight(height)
    weightClassification(weight, height, bodyMassIndex)



#now its time to define our functions
def getWeight(userWeight):
    answer = userWeight
    return userWeight


def getHeight(userHeight):
    userHeight = int(input("Please enter your height: "))
    answer = userHeight
    return userHeight


def weightClassification(userWeight, userHeight, bodyMassIndex):
    bodyMassIndex = userWeight * 703 / userHeight ** 2
    print("Your BMI is: ", bodyMassIndex)

    if bodyMassIndex < 18.5:
        print("You are underweight, go eat a steak")

    elif bodyMassIndex > 18.5 and bodyMassIndex < 25:
        print("Eating healthy must come easy to you, your in your optimal weight range")

    else:
        print("""One of two things happened, either your overweight or you entered in
                some information that isn't computable""")
        answer = input("Do you think you entered information that isn't computable? (Y or N)")

        if answer == 'Y' or answer == 'y':
            print("Then please restart the program and try again")

        else:
            print("Then you are overweight and should consider some lifestyle changes")

main()
