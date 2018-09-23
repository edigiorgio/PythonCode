#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 28, 2018


#This program creates two classes, one superclass and one subclass.
#The subclass uses inheritance to reference the superclass when creating an object.

#This is the superclass "Employee"
class Employee:
    def __init__(self, n, n1): #The initializer method used to initialize an objects data attributes
        self.__name = n
        self.__number = n1

    #Mutators aka setters
    def employee_name(self, n):
        self.__name = n

    def employee_number(self, n1):
        self.__number = n1
    #accessors aka getters
    def return_name(self):
        return self.__name

    def return_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, n, n1, x, z):

        Employee.__init__(self, n, n1) #Calls my employee superclass

        self.__shift = x #initializes my attributes
        self.__hourly = z

    def set_shift(self, x):
        self.__shift = x

    def set_hourly(self, z):
        self.__hourly = z
 
    def get_hourly(self):
        return self.__hourly

    def get_shift(self):
        return self.__shift
    
   
def main():
    #Get the input
    n = input("Enter the employees name: ")
    n1 = input("Enter the employees number: ")
    x = int(input("Please enter shift 1 or shift 2 for the employee:"))
    z = float(input("Please enter the hourly wage for the employee:"))
    #create the object
    worker = ProductionWorker(n, n1, x, z)
    #Display the info of my object
    print('The employee is: ', worker.return_name())
    print('The employee\'s badge number is: ', worker.return_number())
    print('shift is', worker.get_shift())
    print('wage is', worker.get_hourly())

main()
