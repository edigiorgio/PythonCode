#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 1, 2018

#This program accepts 10 golf scores and then sorts them lowest to highest

#Our global list(array)
SCORE = [0,0,0,0,0,0,0,0,0,0]

def main():
    #Call our functions
    getInfo()
    sortScores()    
    displayInfo()
    


def getInfo(): #Gets score info with basic while loop
    index = 0
    while index < len(SCORE):
        SCORE[index] = eval(input("Please enter your 10 most recent scores in any order for me to sort\nPlease enter number " + str(index+1) + ':'))
        index += 1
        
        
def sortScores():
    maxScore = len(SCORE) - 1 #set maxScore to the length of the list - 1
    while maxScore >= 0: #used for comparison purposes
        index = 0 #set for the inner loop
        while index <= maxScore - 1: #This steps through the loop and checks against the element next to it
            if SCORE[index] > SCORE[index + 1]: #This is the comparison
                temp = SCORE[index] #these next three lines swap the elements so there in order
                SCORE[index] = SCORE[index + 1]
                SCORE[index + 1] = temp
            index = index + 1 
        maxScore = maxScore - 1


def displayInfo():
    print("your scores have been sorted, please reference below")
    print(SCORE)
        
main()
