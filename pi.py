# Intro to Programming
# Author: Anthony Griggs
# Date: 9/15/17

import math
bDebugStatements = False

def dprint(message): 
    if (bDebugStatements == True):
        print(message)

print("Note to user: to run program, type 'aproxPi(i)', where i represents a number for how long the sequence should be.")
def aproxPi(i):
    iAnswer =  0
    #This is wrong. Redo.
    #for iCount in range(1, i * 2, 2):
     #   dprint(iCount)

        #for iIn in range(1):
            #This is wierd.
            #iAnswer = iAnswer + (4/iCount - 4/(iCount + 2))
            #iCount = iCount + 2
            #dprint(iCount)
            
        #iAnswer = iAnswer + (4/iCount + 4/(iCount + 2))

    switch = 1
    for iCount in range(1, i * 2, 2):
        #We need to switch between adding and subtracting
        #dprint(iCount)
        if(switch == 1):
            #iAnswer = iAnswer + (4/iCount - 4/(iCount + 2))
            print(iAnswer)
            iAnswer = (iAnswer - 4 / iCount) #Order matters here?
            switch = 2
        else:
            print(iAnswer)
            iAnswer = (iAnswer + 4 / iCount)
            dprint("Switch works")
            switch = 1
        
    print(abs(iAnswer) - math.pi)
    
    
