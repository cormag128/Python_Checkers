# Final Project: Checkers AI
# Written by Thomas Walters and Trevor Jenkins
# The purpose of this project is to demonstrate a complex state-based
# program using heuristic programming to create a Checkers AI capable of
# beating a human in checkershttps://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04https://askubuntu.com/questions/827005/how-to-install-eric-6-on-ubuntu-16-04.

# Import random module for use later in program.
import random

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


# Class to populate and print board.
class Board():
	board = [" " * 8 for i in range(8)]
	error = Errors

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __repr__(self):
		print(self.board)

	#function to place pieces on the board, stri is the name of the pieces
	def placepieces(self, stri):
		#if we want to place white pieces but on bottom 3 rows, use letters array for distinguishing
		#checkers pieces
		wnum = 0;
		bnum = 0;
		letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
		if stri == "W":
			i = self.height - 3
			j = 0
			while i < self.height:
				j = 0
				while j < self.width:
					if i % 2 == 0:
						if j % 2 == 1:
							if wnum < 10:
								self.board[i][j] = "W%s" % letters[wnum]
								wnum += 1
							else:
								self.board[i][j] = "W%s" % letters[wnum]
								wnum += 1
						else:
							pass
					else:
						if j % 2 == 1:
							pass
						else:
							if wnum < 10:
								self.board[i][j] = "W%s" % letters[wnum]
								wnum += 1
							else:
								self.board[i][j] = "W%s" % letters[wnum]
								wnum += 1
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
							if bnum < 10:
								self.board[i][j] = "B%s" % letters[bnum]
								bnum += 1
							else:
								self.board[i][j] = "B%s" % letters[bnum]
								bnum += 1
						else:
							pass
					else:
						if j % 2 == 1:
							pass
						else:
							if bnum < 10:
								self.board[i][j] = "B%s" % letters[bnum]
								bnum += 1
							else:
								self.board[i][j] = "B%s" % letters[bnum]
								bnum += 1
					j += 1
				i += 1

	def setup(self):
		#slashes used as a placeholder for empty spaces
		self.board = [["//" for m in range(8)] for k in range(8)]

		# place white team checkers
		self.placepieces("W")
		#place black team checkers
		self.placepieces("B")

	#print the board itself out, also prints out piece names etc.
	def printboard(self):
		i = 0
		while i < self.height:
			j = 0
			print "---------------------------------------"
			while j < self.width:
				print "|%s|" % (self.board[i][j]),
				j += 1
			print ""
			i += 1
		print "---------------------------------------"

	def move(self,str,move):

		#find the location of the checker we are looking for, could be a function
		#that returns to a checkers class with wval, hval, and str for variables?
		i = 0
		j = 0
		wval = 0
		hval = 0
		while i < self.height:
			j = 0;
			while j < self.width:
				if self.board[i][j] == str:
					hval = i
					wval = j
				j += 1
			i += 1

		#white movement could be split into functions still needs checking for edges
		# needs to handle kings/queens, and no jump handling, jump function could
		# be made and replace the occupied space errors where a jump is possible
		if(str.startswith("W")):
			#moving up and to the right
			if move == 9:
				if self.board[hval - 1][wval + 1] == "//":
					self.board[hval - 1][wval + 1] = self.board[hval][wval]
					self.board[hval][wval] = "//"
					board.printboard()
				#error handling
				else:
					print ("%s") % (self.error.OccupiedSpace)
			# moving up and to the left
			elif move == 7:
				if self.board[hval - 1][wval - 1] == "//":
					self.board[hval - 1][wval - 1] = self.board[hval][wval]
					self.board[hval][wval] = "//"
					board.printboard()
				# error handling
				else:
					print ("%s") % (self.error.OccupiedSpace)
			# error handling for other moves
			elif move == 1:
				print ("%s") % (self.error.BackwardMove)
			elif move == 3:
				print ("%s") % (self.error.BackwardMove)
			else:
				print ("%s") % (self.error.InvalidMove)

		#black movement could be split into functions, still needs checking for edges
		# needs to handle kings/queens, and no jump handling, jump function could
		# be made and replace the occupied space errors where a jump is possible
		elif (str.startswith("B")):
			# moving down and to the left
			if move == 1:
				if self.board[hval + 1][wval - 1] == "//":
					self.board[hval + 1][wval - 1] = self.board[hval][wval]
					self.board[hval][wval] = "//"
					board.printboard()
				#error handling
				else:
					print ("%s") % (self.error.OccupiedSpace)
			# moving down and to the right
			elif move == 3:
				if self.board[hval + 1][wval + 1] == "//":
					self.board[hval + 1][wval + 1] = self.board[hval][wval]
					self.board[hval][wval] = "//"
					board.printboard()
				# error handling
				else:
					print ("%s") % (self.error.OccupiedSpace)
			# error handling
			elif move == 7:
				print ("%s") % (self.error.BackwardMove)
			elif move == 9:
				print ("%s") % (self.error.BackwardMove)
			else:
				print ("%s") % (self.error.InvalidMove)



#start of main function area
#build a board that is 8x8, place checkers and print it out
board = Board(8, 8)
board.setup()
board.printboard()
