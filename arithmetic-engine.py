# CMPT 120
# Author: Anthony Griggs
# 10/13/2017

#AritmeticEngine

#User chooses two numbers

#User chooses what operation happens to those numbers
    #add
    #mult
    #diff
    #quot
    #quit
bLoop = True
def main(bDoLoop):
    while bDoLoop:
        try:
            iFirst = input("Enter a number. Any number! ")
            iSecond = input("Mm. Another! Another number! ")

            iFirst = int(iFirst)
            iSecond = int(iSecond)
            break
        except: #Might be a bit early for exception handling, but I wanted to try this
            print("You did something wrong. Let's try again.")
            bDoLoop = True
            return bDoLoop
    print("Thanks for playing!")

print("This program is an Arimetic Engine.\n"
      "What's-a that?")
while bLoop:
    bLoop = main(bLoop)
