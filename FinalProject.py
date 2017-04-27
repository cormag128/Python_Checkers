# Final Project: Checkers AI
# Written by Thomas Walters and Trevor Jenkins
# The purpose of this project is to demonstrate a complex state-based
# program using heuristic programming to create a Checkers AI capable of
# beating a human in checkershttps://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04.

# Import random module for use later in program.
import random


# Class to populate and print board.
class Board():
	board = [" " * 8 for i in range(8)]

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __repr__(self):
		print(self.board)

	#function to place pieces on the board, stri is the name of the pieces
	def placepieces(self, stri):
		#if we want to place white pieces but on bottom 3 rows
		if stri == "W":
			i = self.height - 3
			j = 0
			while i < self.height:
				j = 0
				while j < self.width:
					if i % 2 == 0:
						if j % 2 == 1:
							self.board[i][j] = stri
						else:
							pass
					else:
						if j % 2 == 1:
							pass
						else:
							self.board[i][j] = stri
					j += 1
				i += 1
		#else we want the black pieces, but on top 3 rows
		else:
			i = 0
			j = 0
			while i < 3:
				j = 0
				while j < self.width:
					if i % 2 == 0:
						if j % 2 == 1:
							self.board[i][j] = stri
						else:
							pass
					else:
						if j % 2 == 1:
							pass
						else:
							self.board[i][j] = stri
					j += 1
				i += 1

	def setup(self):
		#slashes used as a placeholder for empty spaces
		self.board = [["/" for m in range(8)] for k in range(8)]

		# place white team checkers
		self.placepieces("W")
		#place black team checkers
		self.placepieces("B")

	#print the board itself out, also prints out piece names etc.
	def printboard(self):
		i = 0
		while i < self.height:
			j = 0
			print "-------------------------------"
			while j < self.width:
				print "|%s|" % (self.board[i][j]),
				j += 1
			print ""
			i += 1
		print "-------------------------------"


# Class to output different errors that could be encountered during game.
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


#build a board that is 8x8, place checkers and print it out
board = Board(8, 8)
board.setup()
board.printboard()


