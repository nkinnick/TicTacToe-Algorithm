#My attempt. It generates two random moves, but does not print out all the possibilites. I misunderstood the assignment :(


#Building the array for the tic-tac-toe board
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


#Adding lines between each square of the board
def display_board():
  print (board[0] + " | " + board[1] + " | " + board[2])
  print (board[3] + " | " + board[4] + " | " + board[5])
  print (board[6] + " | " + board[7] + " | " + board[8])
  print()

def play_game():

  #Displaying the tic-tac-toe board
  display_board()

  first_turn()

  second_turn()


import random

def first_turn():
 #Generates random position for first move
  position = random.randint(0,8)
  board[position] = "X"
  display_board()


def second_turn():
  positionTwo = random.randint(0,8)
  #If the second move is the same as the first, a new number will be generated until they are different. The position is avaliable when it has a dash.
  while board[positionTwo] != ("-"):
    positionTwo = random.randint(0,8)
  board[positionTwo] = "O"
  display_board()



#Prints out the intial board and both moves
play_game()




"""

#******************************************************
#In class code

import copy

boardCount = 0

allBoards = []
startBoard = [["-","-","-"], ["-","-","-"], ["-","-","-"]]

def printBoard(thisBoard):
  print("Board number: " + str(boardCount))
  for row in thisBoard:
    for item in row:
      print(item, end="")

print()

print("\n******\n")

#Print starting board with noi moves
printBoard(startBoard)

#******************************************************

sBoard = copy.deepcopy(startBoard)

moveOneBoards = []
#Create all boards with 1 move from X
for row in range(0,3):
  for col in range(0,3):
    #Add X to each of the 9 places
    sBoard[row][col] = "X"
    boardCount+=1
    printBoard(sBoard)
    moveOneBoards.append(copy.deepcopy(sBoard))
    sBoard = copy.deepcopy(startBoard)

#******************************************************

moveTwoBoards = []
#Create all bosrds with 2 moves
for board in moveOneBoards: #Iterate through all the 1 move boards
  #Make a working copy of the current board
  wBoard = copy.deepcopy(board)
  #Iterate through all rows and columns
  for row in range(0,3):
    for col in range(0,3):
      #Double check to make sure we aren't overwritting X
      if (wBoard[row][col]== "-"):
        #set row/col to 0
        wBoard[row][col] = "0"
        #Print the board
        boardCount+=1
        printBoard(wBoard)
        #save copy of wBoard to moveTwoBoards list
        moveTwoBoards.append(copy.deepcopy(wBoard))
        wBoard = copy.deepcopy(board)

#******************************************************

moveThreeBoards = []
for board in moveTwoBoards:
  wBoard = copy.deepcopy(board)
  for row in range(0,3):
    for col in range(0,3):
      if (wBoard[row][col]== "-"):
        wBoard[row][col] = "X"
        boardCount+=1
        printBoard(wBoard)
        moveTwoBoards.append(copy.deepcopy(wBoard))
        wBoard = copy.deepcopy(board)
      
      
"""76