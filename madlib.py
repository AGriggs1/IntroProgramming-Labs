# Intro to Programming
# Author: Anthony Griggs
# Date: 9/8/1

def main():
    #Hey now hey now hey now

    #Hm, eval(input()) doesn't seem to like strings
    i = input("1 or 2? ")
    #We need to check if the user input is a digit or a letter, that's our main issue
    if not(str(i) == float(i)): #Doesn't work. i is already a string due to input. 
        eval(input(i))
    nou = input("Enter a noun: ")
    ver = input("Enter a verb: ")
    adj = input("Enter an adjective: " )
    pla = input("Enter a place: ")

    #This I hoped would catch none digits, if it worked, that's what I wanted to see, but uh, see above complaint.
    #That's what it is. WAH! WAH! Python no WORK!
    #i = float(i) or 0 #Darn. This doesn't seem to work. Such a shame :(
    if (str(i) == i):
        print("You think you're smart ya", adj, nou, "go", ver, "off to yur", pla + ". Bleh!")
    else:    
        print("The", adj, nou, "likes to", ver, "at the", pla, "by the by.")
    print("Go home!")
main()
    
    
