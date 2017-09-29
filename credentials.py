# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Anthony Griggs
# Created: 2017-09-29
def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    first = first + "."
    last = input("Enter your last name: ")
    uname = first + last
    # ask user to create a new password
    passwd = input("Create a new password: ")
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")
main()
