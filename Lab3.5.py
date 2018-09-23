#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 3, 2018




#This program asks the user to guess a persons age, weight, and month of birth
#Then this program tests the users input against the "Secret Answers" and displays the results

#This is our main module
def main():

    #From here we declare our variables
    age = int(input("Please enter an age equal to or below my age: "))
    weight = int(input("Please enter a weight equal to or above my weight: "))
    birthMonth = input("Please enter the month you think I was born in: ")

    #Now we will call our functions
    ageFunctions(age)
    weightClass(weight)
    monthOfBirth(birthMonth)
    secretsRevealed(age, weight, birthMonth)


#Now we define our functions that we just called
def ageFunctions(myAge):

    answer = myAge
    return myAge

def weightClass(myWeight):

    answer = myWeight
    return myWeight

def monthOfBirth(myBirthMonth):

    answer = myBirthMonth
    return myBirthMonth

def secretsRevealed(myAge, myWeight, myBirthMonth):
    if myAge <= 29:
        print ("you got it, my age is equal to or less than", myAge)
    else:
        print ("Wrong")

    if myWeight >= 265 and myWeight <= 400:
        print ("You got it, my weight is somewhere around ",myWeight, "give or take")
    else:
        print ("Wrong")

    if myBirthMonth == "August":
        print ("You got it, I was born in August")
    else:
        print ("Wrong")

main()
