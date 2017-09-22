# CMPT 120
# Author: Anthony Griggs
# Date: 9/22/17

sAnimal = "Giraffe"
#tYes[]
#tNo[]
def main():
    bGuess = False
    print("I am thinking of an animal.")

    while (bGuess == False):
        sGuess = input("What animal might it be?\n")
        sGuess = sGuess.capitalize()
      #  print(sGuess)
        if (sGuess == sAnimal):
            print("I'M A GIRAFFE!\n")
            userAns = input("Do... do you like giraffes?\n"
                            "y for yes\n"
                            "n for no\n")
            userAns = userAns[0].lower() #For dummies that can't read ;)
            if(userAns == "y"):
                print("Yay, you like me! You WIN!!!")

            elif(userAns == "n"):
                print("*Sniffle* you're a jerk, you know that? You win.")

            else:
                print("You had one job. Y for yes. N for no. You win, but not at life.") #Extra, I know but I gotta catch those dum-dums
            
            bGuess = True

        elif (sGuess[0] == "Q"): 
            print("Oi, lookie here, another one bites the dust.\n"
                  "You lose.")
            break #You don't even get the satisfaction of bGuess == True!

        else:
            print("Nah. Try again.")
    
main()
