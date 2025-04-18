"""

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password.


added constraints: can only import random and os (to write to file)

added ability to save password to text file
"""
#import random for random numbers
import random as random

#import os to save password to file
import os


#declare global vars
userAn = " "
finalGenPass = " "
randSpecChar = " "

#empty list to hold our initial password
passwordCharList = []

#create a list of commonly accepted special characters for use with random later
specialChars = ["!","#","%","?","@","=",":"]

#function to get get user input
def getUserInput():
    userAn = input("Would you like to generate a new strong password? Enter Y/N: ")
    if userAn.lower() == "y":
        #call genNewPassword function
        genNewPassword()
    elif userAn.lower() == "n":
        print("Exiting, come back later if you need a new password.")
    else:
        print("Invalid input. Please enter Y or N: ")
        getUserInput() #might be better to change to a while in the future

#create function to generate the random password including letters, symbols and numbers. CISA recommends min of 16 chars
def genNewPassword():
    #get the random special character
    randSpecChar = random.choice(specialChars)
    #get 6 random numbers and add them to our password list excluding 0 to avoid confusion with O
    for i in range(6):
        passwordCharList.append(random.randint(1,9))
    #add one special char now
    passwordCharList.append(randSpecChar)
    #add 3 random lowercase letters to our list excluding commonly confused chars i, l o, O and q
    for i in range(3):
        passwordCharList.append(random.choice("abcdefghjkmnoprstuvwxyz"))
    #add 3 cap letters
    for i in range(3):
        passwordCharList.append(random.choice("ABCDEFGHJKLMNPRSTUVWXYZ"))
    #add our final 3 special chars
    for i in range(3):
        passwordCharList.append(random.choice(specialChars))
    #pass the list to our cleanPass to change format
    cleanPass(passwordCharList)


def cleanPass(passwordCharList):
    #declare local vars
    userSaveAn = " "
    #converts list into a string then joins it
    finalGenPass = (''.join(str(x) for x in passwordCharList))
    #prints the password to terminal
    print(finalGenPass)
    
    while True:
        userSaveAn = input("Save Password to file?\nWARNING any existing password file in the local directory will be overwrote\nEnter Y/N: ")
        if userSaveAn.lower() == "y":
            #call savePasstoFile function
            savePasstoFile(finalGenPass)
        elif userSaveAn.lower() == "n":
            print("Exiting, come back later if you need a new password.")
            break
        else:
            print("Invalid input. Please enter Y or N: ")

def savePasstoFile(finalGenPass):
    #local var
    file = ""
    #create password 
    file = open("NewPassword.txt", 'w')
    #write to file
    file.write(finalGenPass)
    #close file
    file.close
    print("Save completed, exiting now.")
    exit()


#main function
def main():
    getUserInput()

if __name__ == "__main__":
    main()