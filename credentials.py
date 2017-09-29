# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Anthony Griggs
# Created: 2017-09-29

def getFullName():
    fullName = []
    # get user's first and last names
    first = input("Enter your first name: ")
    fullName.append(first)
    #first = first + "."
    last = input("Enter your last name: ")
    fullName.append(last)
    return fullName #Should fullName store first and last names separately?

def concatnateName():
    fullName = getFullName() #Fetch the list
    fullName = ".".join(fullName) #Join the names in the list together, replacing the list with a string
    fullName = fullName.lower() 
    return fullName #Return the string

def getPassword():
    passwd = input("Create a new password: ")
    passwd = checkPassword(passwd, 8)
    #while passStrength = checkPassword(passwd): #Let's not...
    #    print("Fool of a Took! That password is feeble!")
    #    passwd = input("Create a new password: ")
    return passwd

def checkPassword(passwd, passLength):
    while len(passwd) < passLength or not(passwd.upper() != passwd and passwd.lower() != passwd): #DeMorgan's suckssssssssss We need (true OR NOT(true|false AND false|true)) to fire loop
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password NOTE: Your password should be upper and lower case, and contain at least 8 characters\n") #The user should know what's up
        #print(passwd.upper(), passwd.upper() == passwd)
        #print(passwd.lower(), passwd.lower() == passwd)
    #print(not(passwd.upper() == passwd and passwd.lower()))
    #print((len(passwd) < passLength and not(passwd.upper() == passwd and passwd.lower() == passwd)))
    return passwd

def main(uname, passwd):
    print("The force is strong in this one...")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

uname = concatnateName()
passwd = getPassword()
main(uname, passwd)

