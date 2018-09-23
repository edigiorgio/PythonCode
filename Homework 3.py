#Eric DiGiorgio
#Homework 3 Exercise 8
#Professor Kodsey
#COP1000
#January 28th 2018

#This is the main function of the program
def main():

    #Declare main variables here
    classAticket = int(input("Please enter the number of Class A tickets sold: "))
    
    classBticket = int(input("Please enter the number of Class B tickets sold: "))
    
    classCticket = int(input("Please enter the number of Class C tickets sold: "))

    #Calling our functions
    aTicketSales = fun1(classAticket)

    bTicketSales = fun2(classBticket)

    cTicketSales = fun3(classCticket)

    #Printing the results of our functions
    print("Your total sales are: ", aTicketSales + bTicketSales + cTicketSales)

def fun1(num1):
    result = num1 * 15
    return result

def fun2(num1):
    result = num1 * 12
    return result

def fun3(num1):
    result = num1 * 9
    return result

main()


    
    
