#Distancetraveledcalculator.py
#Eric DiGiorgio
#Chapter 2 Exercise 5
#January 19, 2018
#This program is an input output game with 3 math questions
#Each question only has one answer and will tell you if you get it right or wrong

#This is my 4 variables being declared and initialized
Distance1 = 300
Distance2 = 480
Distance3 = 720
Name = 0

def main():

    #Display message welcoming you to my game
    print ("Welcome to my little math game")
    print ("Lets test your math skills")

    #First input question
    Name = input ("What is your name? ")
    print ("Thank you ", Name) #Response to input question 1

    #The start of our math questions
    Distance1 = eval (input("""Question 1, if a car is traveling at 60 mph,
how far will it travel in 5 hours? """))
    if Distance1 == 300: #I used if statements to give different outcomes based on answers
        print ("That is correct, good job ", Name)
    else : #Else statements are for anything other than the correct answer
        print ("No ", Name, "The correct answer is 300")
    Distance2 = eval (input("""Question 2, if a car is traveling at 60 mph,
how far will it travel in 8 hours? """))
    if Distance2 == 480:
        print ("That is correct, good job ", Name)
    else :
        print ("No ",Name, "The correct answer is 480")
    Distance3 = eval (input("""Question 3, if a car is traveling at 60mph,
how far will it travel in 12 hours? """))
    if Distance3 == 720:
        print ("That is correct, good job ", Name)
    else :
        print ("No ",Name, "The correct answer is 720")
     #Just a little thank you message for playing   
    print ("Well thank you for playing...")    
