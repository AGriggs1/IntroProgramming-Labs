# CMPT 120
# Author: Anthony Griggs
# Date: 9/22/17

sAnimal = "Giraffe"

def main():
    bGuess = False
    print("I am thinking of an animal.")
    while (bGuess == False):
        sGuess = input("What animal might it be?\n")
        if (sGuess == sAnimal):
            print("I'M A GIRAFFE!\n"
                  "You win.")
            bGuess = True
        else:
            print("Nah. Try again.")
    
