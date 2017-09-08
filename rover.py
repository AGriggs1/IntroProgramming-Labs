# Intro to Programming
# Author: Anthony Griggs
# Date: 9/8/17

## Globals
# mi/s
iLightSpeed = 18600
# In miles
iDistance = 34000000


def GetTimeMarsEarth():
    #Do we want iDistance to be in million miles?
    #No.
    iTime = iDistance / iLightSpeed
    return iTime

GetTimeMarsEarth()
