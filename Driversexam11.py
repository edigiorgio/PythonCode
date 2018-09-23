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


#This function has alot going on I couldn't find any other way to make this work
def questions(pos):
    for words in range(len(DATASETS[0])): #This loops through each item in the list
        tmp = ".)What is the proper procedure when %s" %DATASETS[0][words] #This is the variable used in my if statements
        if DATASETS[3][words] == 'A': #This compares the data in my key to where the proper answer should fall in the choices
            print(str(words + 1) + tmp)
            print('a.)'+str(DATASETS[1][words])+'\nb.)'+random.choice(DATASETS[1])+'\nc.)'+random.choice(DATASETS[1])+'\nd.)'+random.choice(DATASETS[1])) 
        elif DATASETS[3][words] == 'B':
            print(str(words + 1) + tmp)
            print('a.)'+random.choice(DATASETS[1])+'\nb.)'+str(DATASETS[1][words])+'\nc.)'+random.choice(DATASETS[1])+'\nd.)'+random.choice(DATASETS[1]))  
        elif DATASETS[3][words] == 'C': #I cannot keep my random choice function from repeating answers occasionally, I tried shuffle .pop but that just deletes my key and sends back an error after 5 questions
            print(str(words + 1) + tmp)
            print('a.)'+random.choice(DATASETS[1])+'\nb.)'+random.choice(DATASETS[1])+'\nc.)'+str(DATASETS[1][words])+'\nd.)'+random.choice(DATASETS[1]))
        elif DATASETS[3][words] == 'D':
            print(str(words + 1) + tmp)
            print('a.)'+random.choice(DATASETS[1])+'\nb.)'+random.choice(DATASETS[1])+'\nc.)'+random.choice(DATASETS[1])+'\nd.)'+str(DATASETS[1][words]))
        DATASETS[2][words] = input("Please choose carefully\nanswers should all be Capitalized for credit:")
        print('\n')
        
        while DATASETS[2][words].upper() != 'A' and DATASETS[2][words].upper() != 'B' and DATASETS[2][words].upper() != 'C' and DATASETS[2][words].upper() != 'D': # a simple validation loop to make sure acceptable answers are entered
            DATASETS[2][words] = input("Sorry that is not an option, please try again:")
            
          

def answers(pos):
    for words in range(len(DATASETS[0])):
        DATASETS[4] = list(x is y for x, y in zip(DATASETS[2], DATASETS[3]))#This compares my data stored in my key list(x) against my input list(y) to check if it matches and stores it in a new list
    

def displayInfo():
    print("====================END OF TEST====================")
    print("The number of correct answers is " + str(DATASETS[4].count(True)))#prints the amount of true statements
    if DATASETS[4].count(True) >= 15: #if 15 or more true statements exist they passed!
        print("Congratulations you've passed")
        if DATASETS[4].count(True) == 20: #if they got them all right they get a special message
            print("Either you studied really hard... or you cheated, either way go get your picture taken")
    else:
        print("Sorry you have not passed, you need at least 15 right to pass")
        
main()
