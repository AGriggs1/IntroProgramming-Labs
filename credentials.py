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
    return fullName #Return the list

def getPassword(passLength):
    passwd = input("Create a new password: ")
    while len(passwd) < passLength:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return passwd

def main(uname, passwd):
    print("The force is strong in this one...")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

uname = concatnateName()
passwd = getPassword(8)
main(uname, passwd)

