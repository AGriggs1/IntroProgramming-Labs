# Intro to Programming
# Author: Anthony Griggs
# Date: 9/1/17

##################################
# dprint
# enables or disables debug printing
# Simple function used by many, many programmers, I take no credit for it WHATSOEVER
# to enable, simply set bDebugStatements to true!
##NOTE TO SELF: in Python, first letter to booleans are Capitalized
bDebugStatements = True

def dprint(message):
    if (bDebugStatements == True):
        print(message)


#Simple function with no specific purpose
def main():
    dprint("This message is for debugging purposes")
    print("Hello instructor!")
    print("Good bye!")
main()
