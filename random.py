#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 9, 2018

#This program will use the imported function random to generate random numbers that correspond
#to a color that has been assigned to that number
#This program is designed to iterate 10 times and then end itself
#Your job is to try and guess the color that the program generates

#This is to import our random number generator
import random
#Of course this is where we define our main function
def main():
#Follow it up with some print statements to explain the game
    print("Welcome to my ESP game\n")
    print("""The rules are simply
1.)You have 10 tries
2.)You only get one guess per try
3.)Have fun!""")
#because our variables need validation...
    color, guess, count = variables()

#This line is what tells our program to run 10 times... its nifty
    for count in range (10):
        print("Today we will test your ESP abilities")
        print("Please guess a color from the following list(we've already made up our mind, its up to you now)")
        print("Please use the number to the left of the color to make your guess\n")
#This is that validation thing again... oh and it calls my function that generates the number thing        
        color = colorGuess()
        guess = eval(input("0-Red, 1-Blue, 2-Green, 3-Orange, 4-Yellow, 5-Cyan: "))
#This just tells my program to print what "color" it chose based on the number generated
        if color == 0:
            print("My color was Red")
        elif color == 1:
            print("My color was Blue")
        elif color == 2:
            print("My color was Green")
        elif color == 3:
            print("My color was Orange")
        elif color == 4:
            print("My color was Yellow")
        elif color == 5:
            print("My color was Cyan")
#This is just a little message to give the user encouragement
        if guess == color:

            print("You got it, maybe you have some abilities after all\n")

        else:
            print("Looks like you didnt get it this time\n")
   
#These are the functions i've defined for this program... nothing fancy, i like to keep it simple        
def variables():
    color = 0
    guess = 0
    count = 1
    return color, guess, count
#Oh this one is what makes it generate a random number
def colorGuess():
    color = random.randint(0,5)#<---- that right there tells it to stay between 0 and 5 ;-)
    return color
#This makes my program run...
main()
