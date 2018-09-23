#Lab 2.7 Retail tax
#Professor Kodsey
#COP1000
#Eric DiGiorgio


#Defining my main function
def main():
    #below i will be defining my local variables
    totalSales = int(input("Enter the total sales for the month: "))
    countyTax = totalSales * .02
    stateTax = totalSales * .04
    calcTax = stateTax + countyTax
    results(totalSales, countyTax, stateTax, calcTax)

#this is my first function calling for input data to store into my total sales variable
def inputData(totalSales):
    totalSales = int(input("Enter the total sales for the month: "))
    #this is to confirm that the total sales is correct
    return totalSales

#this function is to calculate the county tax paid
def calcCounty(totalSales, countyTax):
    countyTax = totalSales * .02
    print (countyTax)
    return countyTax

#this function is to calculate state tax paid
def calcState(totalSales, stateTax):
    stateTax = totalSales * .04
    return stateTax
        
#this function is to calculate the total tax paid between state and county
def totalTax(totalSales, stateTax, countyTax, calcTax):
    calcTax = stateTax + countyTax
    return calcTax

def results(totalSales, countyTax, stateTax, calcTax):
    print ("your total sales were: ", totalSales)
    print ("your county tax paid on your sales were: ", countyTax)
    print ("your state tax paid on your sales were: ", stateTax)
    print ("The total you paid in taxes were: ", calcTax)

main()
        


