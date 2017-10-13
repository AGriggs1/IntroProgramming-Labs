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
    print("Right-o! I'm going to ask for two numbers from you! Then you get to choose what I do to them by typing either:\n"
          "'add' - adds the two numbers to get the sum!\n"
          "'mult' - multiplys the two numbers to get the product!\n"
          "'diff' - subtracts the two numbers to get the difference!\n" #For now, the order is always first - second
          "'quot' - divides the two numbers to get the quotient!\n" #Ditto
          "\nOtherwise, whenever you're done, just type 'quit' and we can stop!\n"
          "So what are we waiting for? Let's start!") #I'll have this intro here to repeat on reruns of the function in case the user misunderstood something
    while bDoLoop:
        try:
            iFirst = input("Enter a number. Any number! ")
            iSecond = input("Mm. Another! Another number! ")
            print(iSecond + ", " + iFirst + ", those are some nice numbers!")
            iFirst = int(iFirst)
            iSecond = int(iSecond)
            sCommand = input("Okay, what do you want me to do with these fab numbers? ")
            #Seperate function?
            sCommand = str(sCommand).lower()
            Result = "- oh! Sorry, I don't recognize this command. K we're done here LUL." #in case all if statements fail
            if sCommand == "add":
                Result = iFirst + iSecond #Hybrid int and string, not sure what notation to use
            elif sCommand == "mult":
                Result = iFirst * iSecond
            elif sCommand == "diff":
                #Result = (iFirst and iSecond) - (iFirst or iSecond) #Stumbled on this last week, had to test it
                Result = iFirst - iSecond
            elif sCommand ==  "quot":
                Result = iFirst / iSecond
            elif sCommand == "quit":
                Result = "- oh, okay! I hope you had fun!"
                bDoLoop = False
            else:
                bDoLoop = False
            #print the result
            print("That's", Result)
                

        except: #Might be a bit early for exception handling, but I wanted to try this
            print("Oh wait, what am I saying? Those are horrible! You did something wrong. Let's try again.") #Vague
            bDoLoop = True
            return bDoLoop
    print("Thanks for playing!")
    return bDoLoop

print("This program is an Arimetic Engine.\n"
      "What's-a that?")
while bLoop:
    bLoop = main(bLoop)
