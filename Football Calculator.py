#Lab 1-5
# this is a program to calculate the average of wins over 5 years
# Eric DiGiorgio COP1000 Professor Kodsey
year1 = int
year2 = int
year3 = int
year4 = int
year5 = int

#This is where we will ask for our input for the variables defined above

year1 = int (input("Enter wins for the first year: "))
year2 = int (input ("Enter wins for the second year: "))
year3 = int (input ("Enter wins for the third year: "))
year4 = int (input ("Enter wins for the fourth year: "))
year5 = int (input ("Enter wins for the fifth year: "))

#Declare the last variable to calculate the average wins
averagewins = (year1 + year2 + year3 + year4 + year5)/5

#This is the output of the resulting program

print ("The average wins for 5 years is: ", averagewins)



