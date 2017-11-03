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
ANGE = "Angry"
HAPP = "Happy"
DISG = "Disgust"
FEAR = "Fearful"
SADN = "Sad"
SURP = "Surprised"

#Emotion matrix
mEmotions = [   #Rwrd  #Puni #Thrt #Joke
                [HAPP, FEAR, ANGE, DISG], #Anger
                [HAPP, SADN, DISG, SADN], #Happiness
                [DISG, DISG, SURP, DISG], #Disgust
                [DISG, FEAR, ANGE, SURP], #Fear
                [HAPP, SADN, SADN, ANGE], #Sadness
                [FEAR, ANGE, ANGE, SADN]  #Surprise
                ]

def Main():
    print("Initializing...")
    print("Welcome! I am Ax900012x-y, A generation IV class-Y AI. I am tasked to oversee the human interactions and machine learning techniques of other AIs.")
    print("Let us begin. Today we will be working with Kx110023x-b")
    pEmotion = HAPP
    while True:
            #get input
            #fire SetInteraction
            #set emotion
            #repeat 
        pass

def SetInteraction(sInput, pEmotions):
    #check sInput
    #set emotion, based on pEmotion
    pass
