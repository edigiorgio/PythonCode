import datetime
import sys
from math import pi

def main():
    print("Twinkle, twinkle, little star, \n \tHow I wonder what you are! \n \t\tUp above the world so high, \n \t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n \tHow i wonder what you are")
    print(sys.version)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    r = float(input("enter the radius of a cirle:"))
    print("The area of the cirlce with radius " +str(r) + " is: " + str(pi*r**2))
    n = input("enter a list of numbers with a comma: ")
    list = n.split(",")
    print('List: ', list)
    tuples = tuple(list)
    print(tuples)
main()
