#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#February 28,2018

#This is a multiple choice test that uses a list with multiple elements
#There are alot of notes in this program to help explain as well as help me remember how and why i did what i did.

#This is currently my favorite built in function, it accomplishes alot
import random

#This is my multiple list, it has 5 elements the first being to change the questions asked, the second to change the answers, the third for input and the 4th for storing correct vs incorrect answers
DATASETS = [["You first enter the car", "You start the car","You reverse","You turn",
             "Coming to a yellow light","You get cut off","You run over a person","You have to stop short",
             "in a high speed chase","in a stolen car","A light is broken","The car next to you breaks down",
             "You get a text message","You get a call","Your out of gas","Late for work","Driving angry",
             "Someone flips you the bird","Your speedometer stops working","Drinking"],
            ["Put on seat belt","Check your mirrors","Look over your shoulder","Use your turn signal",
             "Slow to a safe stop","Relax and dont get upset","Call 911", "Thank your brakes for working",
             "Pull over and give up","Ask to get out","Get it fixed","Offer help","Ignore it","Ignore it",
             "Get gas... duh","Drive the speed limit","Don't do it","Smile and wave","Get it fixed","Don't do it"],
            [''] * 20,
            ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A'],
            [''] * 20]
#A call to main to run my program
def main():
    #A call to our functions
    questions(0)
    answers(1)
    displayInfo()
    
#This function has alot going on and is currently incomplete, the goal is to use different loops to change the position of the correct answer
def questions(pos):
    for words in range(len(DATASETS[0])):        
        tmp = "\n" + str(words + 1) + ".)What is the proper procedure when %s" %DATASETS[0][words] + '\nA.)'
        if DATASETS[3][words] == 'A': #if the answer key is A
            tmp = tmp + DATASETS[1][words] #append the first choice as correct choice
        else:
            tmp = tmp + random.choice(DATASETS[1])


def answers(pos):
    for words in range(len(DATASETS[0])):
        DATASETS[4] = list(x is y for x, y in zip(DATASETS[2], DATASETS[3]))
    

def displayInfo():
    print("====================END OF TEST====================")
    print("The number of correct answers is " + str(DATASETS[4].count(True)))
    if DATASETS[4].count(True) >= 15:
        print("Congratulations you've passed")
        if DATASETS[4].count(True) == 20:
            print("Either you studied really hard... or you cheated, either way go get your picture taken")
    else:
        print("Sorry you have not passed, you need at least 15 right to pass")
        
