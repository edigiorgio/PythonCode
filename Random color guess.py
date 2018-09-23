#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 9, 2018


#
#


#
import random

def main():

    color, name, guess, count = variables()


    if count < 10:

        print("Today we will test your ESP abilities")
        print("""Please guess a color from the following list(by the way we've already
                made up our mind, its up to you to guess)""")

        guess = eval(input("""Please use the number to the left of the color to make
                            your guess
                            0-Red
                            1-Blue
                            2-Green
                            3-Orange
                            4-Yellow
                            5-Cyan
                            :""")

        if guess == color
                     print("You got it, maybe you have some abilities after all")
                     return
        else
                     print("Looks like you didn't get it this time")
                     return

        count()

def variables():
                     color = 0
                     name = ""
                     guess = 0
                     count = 0



                    
