#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#April 22, 2018

import sys #Used for exit functions
import random #Used for random choice from the computer
from time import sleep #used to pause the program at certain times 
import os #Used to clear player 1 selection in 2 player mode
#This program is a rock paper scissors style game


WEAPONS = ["Rock", "Paper", "Scissors"] #Global weapons for the computer to choose from

def main():
    #Local variables for scores, selections etc.
    compScore = 0
    playScore1 = 0
    playScore2 = 0
    choice1 = 0
    choice2 = 0
    print("Welcome to rock paper scissors!")#Welcome message
    while True:
        try:
            choice1 = int(input("""Please make a selection below\n1.)See the Rules\n2.)Play against the computer
3.)Play a two player game\n4.)Quit\nmake selection:""")) #Menu selection
            print()
        except ValueError:
            choice1 = int(input("Not a recognized selection, try again:"))
            print()
            continue
        else:
            if choice1 == 1:
                sleep(1)
                showRules()
            elif choice1 == 2:
                playComputer(compScore, playScore1)
            elif choice1 == 3:
                playFriend(playScore2, playScore1)
            elif choice1 == 4:
                sys.exit()

#Function to explain the rules
def showRules():
    print("Welcome to the rule book for rock paper scissors!")
    sleep(1)
    print("""The rules are simple, you will make a selection using 1-3 and the computer
will make a random selection as well, your selections will be compared and then the results will display
the winner gets a point and the option to play another round will be displayed.
I think its important to mention that in 2 player mode the screen clears after player 1 makes a selection to avoid
any temptations of cheating! Good Luck!""")
    sleep(10) #Sleep timer to allow you to read the rules
    print()
    main()

def playComputer(compScore, playScore1): #Computer mode
    endProgram = 'yes'
    while endProgram == 'yes':
        while True:
            try:
                choice2 = int(input("""Please choose your weapon from the menu below\n1.)Rock
2.)Scissors\n3.)Paper\n4.)Main Menu\nmake selection:"""))#Weapon selection
                print()
            except ValueError:
                choice2 = int(input("Not a valid response, try again:"))
                print()
                continue
            else:                    
                if choice2 == 4:
                    main()
                else:
                    computer = random.choice(WEAPONS) #Computer random choice
                    print("The computer chooses " + computer)
                    if computer == "Rock" and choice2 == 1:
                        print()
                        print('You tied with the computer')
                        print()
                    elif computer == "Rock" and choice2 == 2:
                        print()
                        print('The computers rock beats your scissors')
                        print()
                        compScore += 1
                    elif computer == "Rock" and choice2 == 3:
                        print()
                        print('Your paper beats the computers rock')
                        print()
                        playScore1 += 1
                    elif computer == "Paper" and choice2 == 1:
                        print()
                        print("The computers paper beats your rock")
                        print()
                        compScore += 1
                    elif computer == "Paper" and choice2 == 2:
                        print()
                        print("Your Scissors beats the computers paper")
                        print()
                        playScore1 += 1
                    elif computer == "Paper" and choice2 == 3:
                        print()
                        print("Your tied with the computer")
                        print()
                    elif computer == "Scissors" and choice2 == 1:
                        print()
                        print("Your rock beats the computers scissors")
                        print()
                        playScore1 += 1
                    elif computer == "Scissors" and choice2 == 2:
                        print()
                        print("You tied with the computer")
                        print()
                    elif computer == "Scissors" and choice2 == 3:
                        print()
                        print("The computers scissors beats your paper")
                        print()
                        compScore += 1
                print('The current score is\nPlayer:' + str(playScore1) + '\nComputer:' + str(compScore))
                sleep(1)
                print()
                sleep(1)
                print()
                endProgram = input("Would you like to play again?(yes or no)")
                if endProgram == 'no':
                    print()
                    print()
                    print()
                    main()
                    return compScore, playScore1

def playFriend(playScore2, playScore1): #Two player mode
    endProgram = 'yes'
    while endProgram == 'yes':
        while True:
            try:
                choice2 = int(input("""Player 1 please choose your weapon from the menu below\n1.)Rock
2.)Scissors\n3.)Paper\n4.)Main Menu\nmake selection:"""))
                print()
            except ValueError:
                choice2 = int(input('That input is not valid, try again:'))
                print()
                continue
            else:
                if choice2 == 4:
                    main()
                os.system('CLS') #Used to clear the screen between selections to avoid cheating. only works in DOS prompt
                while True:
                    try:
                        choice3 = int(input("""Player 2 Please choose your weapon from the menu below\n1.)Rock
2.)Scissors\n3.)Paper\n4.)Main Menu\nmake selection:"""))
                        print()
                    except ValueError:
                        choice3 = int(input('That input is not valid, try again:'))
                        print()
                        continue
                    else:
                        if choice3 == 4:
                            main()
                        else:
                            if choice3 == 1 and choice2 == 1:
                                print()
                                print('You tied')
                                print()
                            elif choice3 == 1 and choice2 == 2:
                                print()
                                print('Rock beats scissors')
                                print()
                                playScore2 += 1
                            elif choice3 == 1 and choice2 == 3:
                                print()
                                print('Paper beats rock')
                                print()
                                playScore1 += 1
                            elif choice3 == 3 and choice2 == 1:
                                print()
                                print("Paper beats rock")
                                print()
                                playScore2 += 1
                            elif choice3 == 3 and choice2 == 2:
                                print()
                                print("Scissors beats paper")
                                print()
                                playScore1 += 1
                            elif choice3 == 3 and choice2 == 3:
                                print()
                                print("You tied")
                                print()
                            elif choice3 == 2 and choice2 == 1:
                                print()
                                print("Rock beats scissors")
                                print()
                                playScore1 += 1
                            elif choice3 == 2 and choice2 == 2:
                                print()
                                print("You tied")
                                print()
                            elif choice3 == 2 and choice2 == 3:
                                print()
                                print("Scissors beats paper")
                                print()
                                playScore2 += 1
                        print('The current score is\nPlayer 1:' + str(playScore1) + '\nPlayer 2:' + str(playScore2))
                        sleep(1)
                        print()
                        sleep(1)
                        print()
                        endProgram = input("Would you like to play again?(yes or no)")
                        if endProgram == 'no':
                            print()
                            print()
                            print()
                            main()
                            return playScore2, playScore1    
main()

