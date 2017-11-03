# Intro to Programming
# Author: Anthony Griggs
# Date: 11/3 2017

#emotions: anger, disgust, fear, happiness, sadness, surprise
#actiones: reward, punish, threaten, joke

#anger > (reward)happiness
#anger > (punish)fear
#anger > (threaten)anger
#anger > (joke)digust

#happiness > (reward)happiness
#happiness > (punish)sadness
#happiness > (threaten)disgust
#happiness > (joke)sadness

#disgust > (reward)disgust
#disgust > (punish)disgust
#disgust > (threaten)surprise
#disgust > (joke)disgust

#fear > (reward)disgust
#fear > (punish)fear
#fear > (threaten)anger
#fear > (joke)surprise

#sadness > (reward)happiness
#sadness > (punish)sadness
#sadness > (threaten)sadness
#sadness > (joke)anger

#surprise > (reward)fear
#surprise > (punish)anger
#surprise > (threaten)anger
#surprise > (joke)sadness

#Row Indexes
iAnger = 0
iHappy = 1
iDisgust = 2
iFear = 3
iSad = 4
iSurprise = 5
#Column Indexes
iReward = 0
iPunish = 1
iThreaten = 2
iJoke = 3
#Constants (To make the matrix look clean), I'll flesh these out as need be
ANGE = "Grrrrrrrr!!!"
HAPP = "Yay!"
DISG = "You're gross."
FEAR = "Get away from me creep!"
SADN = "Now I'm sad. Buy me stuff"
SURP = "!"


#Emotion matrix
mEmotions = [   #Rwrd  #Puni #Thrt #Joke
                [HAPP, FEAR, ANGE, DISG], #Anger
                [HAPP, SADN, DISG, SADN], #Happiness
                [DISG, DISG, SURP, DISG], #Disgust
                [DISG, FEAR, ANGE, SURP], #Fear
                [HAPP, SADN, SADN, ANGE], #Sadness
                [FEAR, ANGE, ANGE, SADN]  #Surprise
                ]
kid = "Kid:"
def Main():
    print("Initializing...")
    print("Welcome! I am Ax900012x-y, A generation IV class-Y AI. I am tasked to oversee the human interactions and machine learning techniques of other AIs.")
    print("Let us begin. Today we will be working with Kx110023x-b")
    input("You can either choose to 'Reward', 'Punish', 'Threaten', or 'Joke' towards Kx110023x-b, or 'Kid'\nPress enter when ready.")
    pEmotion = HAPP
    print(kid, "Hi! I'm kid! Nice to meet ya!")
    while True:
            print(kid, pEmotion)
            sInput = input("Choose an interaction: ").lower()
            sInput or "None"
            print(sInput)
            pEmotion = SetInteraction(sInput, pEmotion)
            #repeat
            
def GetEmotionIndex(pEmotion):
#I don't have the cognitive power atm to come up with a more efficient method, so I'm doing what I know works
    if pEmotion == ANGE:
        return iAnger

    elif pEmotion == HAPP:
        return iHappy

    elif pEmotion == DISG:
        return iDisgust

    elif pEmotion == FEAR:
        return iFear

    elif pEmotion == SADN:
        return iSad

    elif pEmotion == SURP:
        return iSurprise

    return None #This should never happen BUT
def SetInteraction(sInput, pEmotion):
    if sInput == "reward":
        pEmotion = mEmotions[GetEmotionIndex(pEmotion)][iReward]

    elif sInput == "punish":
        pEmotion = mEmotions[GetEmotionIndex(pEmotion)][iPunish]

    elif sInput == "threaten":
        pEmotion = mEmotions[GetEmotionIndex(pEmotion)][iThreaten]

    elif sInput == "joke":
        pEmotion = mEmotions[GetEmotionIndex(pEmotion)][iJoke]

    else:
        print("Sorry, your interaction could not be understood.")
    #return emotion
    return pEmotion

def ShowInteraction(sInput, pEmotion):
    #print AI reaction / emotion, probably the latter
    print(kid, pEmotion)
