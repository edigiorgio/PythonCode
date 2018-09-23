#Eric DiGiorgio
#COP 1000
#Professor Kodsey
#March 21, 2018

import sys
from time import sleep

storedPassword = 'Password'
prompt = ''
option = ''
output = ''
userPassword = ''
readData = ''
input1 = ''

#This is an encryption/decryption program. You will need to set a password, once
#your password is set you will use it to lock/unlock your files. everything you enter
#will encrypted and transfered to a file. Enjoy


def main():
    choice = 0
    print("Welcome to the encryption/decryption program")
    sleep(1)
    print("Please make a selection below")
    sleep(1)
    print("1.)Encrypt some text")
    print("2.)Decrypt whats in the file")
    print("3.)Change your password")
    print("4.)Exit the program")
    
    choice = eval(input("Please make your selection:"))

    if choice == 1:
        enterEncryption(input1)
    elif choice == 2:
        decryptFile(output)
    elif choice == 3:
        changePassword()
    elif choice == 4:
        sys.exit()
    else:
        print("Oops something went wrong \nRestarting program")
        main()


    
def getPassword():
    global storedPassword
    attempts = 3
    counter = 0
    print("This program is password protected, you have 3 attempts at the password before the system exits")
    sleep(1)
    print("***HINT***\nTry Password(Case sensitive)")
    sleep(1)
    userPassword = input('Please enter your Password:')
    if userPassword == storedPassword:
        main()
    else:
        while counter != 3:
            userPassword = input('That was incorrect you have ' + str(attempts-counter) + ' attempts left:')
            counter += 1
            if userPassword == storedPassword:
                main()
            if counter == 3:
                sys.exit()

def changePassword():
    continue1 = ''
    print("This is to change your stored password")
    global storedPassword
    storedPassword = input("Please enter your new password:")
    encryptionFile = open('secrets1.txt', 'a')
    encryptionFile.write(str(storedPassword) + '\n')
    encryptionFile.close()
    continue1 = input("Would you like to continue the program(yes or no)").lower()
    if continue1 == 'yes':
        main()
    elif continue1 == 'no':
        sys.exit()
    else:
        print("I didnt understand that")
        changePassword()
                          
    
def enterEncryption(input1):
    continue1 = 'yes'
    print("Any data entered here will be encrypted and written to a file")
    while continue1 == 'yes':
        prompt = input("Please enter what you want encrypted:")
        for i in range(0, len(prompt)):
            input1 = input1 + chr(ord(prompt[i]) - 2)
        encryptionFile = open('secrets1.txt', 'a')
        encryptionFile.write(str(input1) + '\n')
        encryptionFile.close()
        continue1 = input("Would you like to input anything else(yes or no):").lower()
        input1 = ''
    continue1 = input("Would you like to continue the program(yes or no)").lower()
    if continue1 == 'yes':
        main()
    elif continue1 == 'no':
        sys.exit()
    else:
        print("I didnt understand that")
        enterEncryption()

def decryptFile(output):
    continue1 = ''
    encryptionFile = open('secrets1.txt', 'r')
    readData = encryptionFile.readline()
    readData = readData.rstrip('\n')
    for x in range(len(readData)):
        output = output + chr(ord(readData[x]) + 2)
    print(output)
    encryptionFile.close()
    continue1 = input("Would you like to continue the program(yes or no)").lower()
    if continue1 == 'yes':
        main()
    elif continue1 == 'no':
        sys.exit()
    else:
        print("I didnt understand that")
        decryptFile()

getPassword()
