#Final Project: Checkers AI
#Written by Thomas Walters and Trevor Jenkins
#The purpose of this project is to demonstrate a complex state-based
#program using heuristic programming to create a Checkers AI capable of 
#beating a human in checkershttps://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04.

#Import random module for use later in program.
import random
#Class to populate and print board.
class Board():    
    board = [[0]*8 for i in range(8)]

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __repr__(self):
        print(self.board)

    def setup(self):
        board = [[0]*self.height for i in range(self.width)]
        
#Class to output different errors that could be encountered during game.
class Errors:
	NotValid = "The space entered is not a valid move."
	ShortMove = "Move must start at current position and finish at another square."
	WrongPiece = "Player must move their own piece."
	OccupiedSpace = "Player must move to an empty space."
	MoveTooLong = "Player must move exactly two spaces."
	BackwardMove = "Only king can move backward."
	MustJump = ("Player must jump opponent in this move, and must do multiple jumps"
		    "if they are possible.")
	KingPiece = "Move terminates immediately if piece enters king's row."
	JumpMove = "If a move starts with a jump, only jumps can be performed."
	InvalidCapture = "Player can only capture opponent's pieces."
	InvalidMove = "Please move to an adjacent empty space, or jump the opponent."





board = Board(8,8)
board.setup()
for row in Board.board:
	print (row)





