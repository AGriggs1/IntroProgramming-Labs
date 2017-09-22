# CMPT 120
# Author: Anthony Griggs
# Date: 9/22/17

sAnimal = "Giraffe"

def main():
    bGuess = False
    print("I am thinking of an animal.")
    while (bGuess == False):
        sGuess = input("What animal might it be?\n")
        sGuess = sGuess.capitalize()
      #  print(sGuess)
        if (sGuess == sAnimal):
            print("I'M A GIRAFFE!\n"
                  "You win.")
            bGuess = True
        elif (sGuess == "Quit"): #WHAT? elif?! Gh.
            print("Oi, lookie here, another one bites the dust.\n"
                  "You lose.")
            break #You don't even get the satisfaction of bGuess == True!
        else:
            print("Nah. Try again.")
    
main()
