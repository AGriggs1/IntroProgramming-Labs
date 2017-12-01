
# CMPT 120
# Author: Anthony Griggs
# 10/13/2017

from graphics import *
#import graphics #for whatever reason this doesn't import anything
#It'll import, just nothing from the file its importing will work
#AritmeticEngine

#User chooses two numbers

#User chooses what operation happens to those numbers
    #add
    #mult
    #diff
    #quot
    #quit
bLoop = True
def drawResult(point, text, window):
    pResult = Text(point, text)
    pResult.draw(window)
pWindow = GraphWin("Arithmetic Engine", 600, 400)
pWindow.setCoords(0, 0, 10, 8)
def main(bDoLoop):
    #Define intro statement
    pIntro = Text(Point(5, 6), "Righty! I'm going to ask you for TWO numbers! Then you tell what to do with them!\n\n"
                               "'add' - adds the two numbers to get the sum!\n"
                               "'mult' - multiplays the two numbers to get the difference!\n"
                               "'diff' - subtracts the two numbers to get the difference!\n"
                               "'quot' - divides the two numbers to get the quotient!\n\n"
                               "So, uh, let's start! Click the screen, would ya?")
    #Resize                    
    pIntro.setSize(10)
    #Wait for return key
    pIntro.draw(pWindow)
    while (pWindow.getMouse() == None): pass
    
    #undraw
    pIntro.undraw()
    pIntro.setText("'add' - adds the two numbers to get the sum!\n"
                   "mult - multiplays the two numbers to get the difference!\n"
                   "diff - subtracts the two numbers to get the difference!\n"
                   "quot - divides the two numbers to get the quotient!\n\n"
                   "quit - quits the game!")
    #redraw
    pIntro.draw(pWindow)
    #Define entry boxes
    pEntryOne = Entry(Point(3, 4), 10)
    pEntryOne.setText("#1")
    pEntryOne.draw(pWindow)
    pEntryTwo = Entry(Point(3 ,3), 10)
    pEntryTwo.setText("#2")
    pEntryTwo.draw(pWindow)

    #Define Buttons
    pAdd = Rectangle(Point(5, 4), Point(7, 3))
    pTextAdd = Text(pAdd.getCenter(), "Add")
    pAdd.draw(pWindow)
    pTextAdd.draw(pWindow)
    pSub = Rectangle(Point(5, 3), Point(7, 2))
    pTextSub = Text(pSub.getCenter(),"Diff")
    pSub.draw(pWindow)
    pTextSub.draw(pWindow)
    pMul = Rectangle(Point(7, 4), Point(9, 3))
    pTextMul = Text(pMul.getCenter(), "Mult")
    pMul.draw(pWindow)
    pTextMul.draw(pWindow)
    pDiv = Rectangle(Point(7, 3), Point(9, 2))
    pTextDiv = Text(pDiv.getCenter(), "Quot")
    pDiv.draw(pWindow)
    pTextDiv.draw(pWindow)
    pQuit = Rectangle(Point(2, 2), Point(4, 1))
    pTextQuit = Text(pQuit.getCenter(), "Quit")
    pQuit.draw(pWindow)
    pTextQuit.draw(pWindow)
    iResult = 0
    pResult = Text(Point(4.5, 1), str(iResult))
    print("Right-o! I'm going to ask for two numbers from you! Then you get to choose what I do to them by typing either:\n"
          "'add' - adds the two numbers to get the sum!\n"
          "'mult' - multiplys the two numbers to get the product!\n"
          "'diff' - subtracts the two numbers to get the difference!\n" #For now, the order is always first - second
          "'quot' - divides the two numbers to get the quotient!\n" #Ditto
          "\nOtherwise, whenever you're done, just type 'quit' and we can stop!\n"
          "So what are we waiting for? Let's start!") #I'll have this intro here to repeat on reruns of the function in case the user misunderstood something
    
    
    
    while bDoLoop:
        iResult = 0
        pCoords = pWindow.getMouse()
        pResult.setText(str(iResult))
        pResult.undraw()
        pResult.draw(pWindow)
        pResult.undraw()
        pNumOne = pEntryOne.getText()
        pNumTwo = pEntryTwo.getText()
        try:
            iNumOne = int(pNumOne)
            iNumTwo = int(pNumTwo)
        except:
            print("Those are not numbers!") #I KNOW THIS DOESN'T APPEAR IN THE WINDOW
            if ((pCoords.getX() > pQuit.getP1().getX() and pCoords.getY() < pQuit.getP1().getY()) and (pCoords.getX() < pQuit.getP2().getX() and pCoords.getY() > pQuit.getP2().getY())):
                pWindow.close()
                bDoLoop = False
                print("Sod one will ya?")
                #I'm lazy. And very bitter right now.
            continue

        if ((pCoords.getX() > pAdd.getP1().getX() and pCoords.getY() < pAdd.getP1().getY()) and (pCoords.getX() < pAdd.getP2().getX() and pCoords.getY() > pAdd.getP2().getY())):
            print("add")
            iResult = iNumOne + iNumTwo
            pResult.setText(str(iResult))
            pResult.draw(pWindow)
        elif ((pCoords.getX() > pSub.getP1().getX() and pCoords.getY() < pSub.getP1().getY()) and (pCoords.getX() < pSub.getP2().getX() and pCoords.getY() > pSub.getP2().getY())):
            print("sub")
            iResult = iNumOne - iNumTwo
            pResult.setText(str(iResult))
            pResult.draw(pWindow)
        elif ((pCoords.getX() > pMul.getP1().getX() and pCoords.getY() < pMul.getP1().getY()) and (pCoords.getX() < pMul.getP2().getX() and pCoords.getY() > pMul.getP2().getY())):
            print("molyneux lies again")
            iResult = iNumOne * iNumTwo
            pResult.setText(str(iResult))
            pResult.draw(pWindow)
        elif ((pCoords.getX() > pDiv.getP1().getX() and pCoords.getY() < pDiv.getP1().getY()) and (pCoords.getX() < pDiv.getP2().getX() and pCoords.getY() > pDiv.getP2().getY())):
            print("div")
            iResult = iNumOne / iNumTwo
            pResult.setText(str(iResult))
            pResult.draw(pWindow)
        elif ((pCoords.getX() > pQuit.getP1().getX() and pCoords.getY() < pQuit.getP1().getY()) and (pCoords.getX() < pQuit.getP2().getX() and pCoords.getY() > pQuit.getP2().getY())):
            pWindow.close()
            bDoLoop = False
            print("Sod one will ya?")
        
        #
        #try:
          #  iFirst = input("Enter a number. Any number! ")
          #  iSecond = input("Mm. Another! Another number! ")
          #  print(iSecond + ", " + iFirst + ", those are some nice numbers!")
          #  iFirst = int(iFirst)
          #  iSecond = int(iSecond)
          #  sCommand = input("Okay, what do you want me to do with these fab numbers? ")
            #Seperate function?
          #  sCommand = str(sCommand).lower()
          #  Result = "- oh! Sorry, I don't recognize this command. K we're done here LUL." #in case all if statements fail
          #  if sCommand == "add":
          #      Result = iFirst + iSecond #Hybrid int and string, not sure what notation to use
          #  elif sCommand == "mult":
          #      Result = iFirst * iSecond
          #  elif sCommand == "diff":
          #      #Result = (iFirst and iSecond) - (iFirst or iSecond) #Stumbled on this last week, had to test it
          #      Result = iFirst - iSecond
          #  elif sCommand ==  "quot":
          #      Result = iFirst / iSecond
          #  elif sCommand == "quit":
          #      Result = "- oh, okay! I hope you had fun!"
          #      bDoLoop = False
          #  else:
          #      bDoLoop = False
            #print the result
          #  print("That's", Result)
                

       # except: #Might be a bit early for exception handling, but I wanted to try this
       #     print("Oh wait, what am I saying? Those are horrible! You did something wrong. Let's try again.") #Vague
       #     bDoLoop = True
       #     return bDoLoop
    print("Thanks for playing!")
    return bDoLoop

print("This program is an Arimetic Engine.\n"
      "What's-a that?")
while bLoop:
    bLoop = main(bLoop)
