# CMPT 120 Intro to Programming
# Lab 6 - Lists and Error Handling
#Author: Your name here
# 10/27/2017

symbol = [" ", "x", "o"]

def printBoard(board):
    #print the top border
    border = "+-----------+"
    print(border)
    for row in board:
        s = "| "
        for col in row:
            s = s + symbol[col] + " | " 
            
        print(s)
        print(border)

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
        #if true set square to player number/symbol
    if board[row][col] == 0:
        board[row][col] = player

def getPlayerMove():
    
    while True:
        r = int(input("Row? ") or -1)  #If the player inputs nothing convert it to -1
        c = int(input("Column? ") or -1) #ask user seperately for the row and column number
        if not(r < 0 and c < 0 or r > 2 and c > 2): #Check to make sure r and c are in proper range
            break
        print("Please input numbers between 0 and 2")
    return (r,c) #return row and column number

def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return True
        #for each square in the row:
            #check whether the square is blank
                # if True return True
    printBoard(board)
    return False #else return False

def main():
    board = [
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
            ]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1 #player = player is x and y or x where x = 1, y = 2
                                
main()
