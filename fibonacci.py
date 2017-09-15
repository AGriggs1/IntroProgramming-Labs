# Intro to Programming
# Author: Anthony Griggs
# Date: 9/15/17

bDebugStatements = False

def dprint(message): #Find out how to do unlimited parameters!
    if (bDebugStatements == True):
        print(message)
print("Note to user: to run program, type 'fibonacci(i)', where i represents a number for how long the sequence should be.")

def fibonacci(i):
    iCurrent = 1
    iAnswer = 0
    
    for iCount in range(i):
      iAnswer = iCurrent + iAnswer
      dprint(iAnswer)
      iCurrent = iAnswer - iCurrent

    return iAnswer

    
