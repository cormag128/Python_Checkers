# Final Project: Checkers AI
# Written by Thomas Walters and Trevor Jenkins
# The purpose of this project is to demonstrate a complex state-based
# program using heuristic programming to create a Checkers AI capable of
# beating a human in checkers

# Import random module for use later in program.
import random
import string

# Class to output different errors that could be encountered during game.
class Errors:
	NotValid = "The space entered is not a valid move."
	ShortMove = "Move must start at current position and finish at another square."
	WrongPiece = "Player must move their own piece."
	OccupiedSpace = "Player must move to an empty space."
	MoveTooLong = "Player must move exactly two spaces."
	BackwardMove = "Only king can move backward."
	MustJump = "Player must jump opponent in this move, and must do multiple jumps, if possible."
	KingPiece = "Move terminates immediately if piece enters king's row."
	JumpMove = "If a move starts with a jump, only jumps can be performed."
	InvalidCapture = "Player can only capture opponent's pieces."
	InvalidMove = "Please move to an adjacent empty space, or jump the opponent."
	OutofBounds = "That move is out of bounds. Please choose another move."


# Class to populate and print board.
class Board():
	board = [" " * 8 for i in range(8)]
	error = Errors
	turn = 'W'
	winState = 'N'
	blackPieces = 12
	whitePieces = 12

	def __init__(self, width, height):
		self.width = width
		self.height = height
		

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
		self.board = [["  " for m in range(8)] for k in range(8)]

		# place white team checkers
		self.placepieces("W")
		#place black team checkers
		self.placepieces("B")

	#print the board itself out, also prints out piece names etc.
	def printboard(self):
		i = 0
		print "\n\n\n\n"
		while i < self.height:
			j = 0
			print "---------------------------------"
			while j < self.width:
				print "|%s" % (self.board[i][j]),
				j += 1
			print "|"
			i += 1
		print "---------------------------------"

	def kingme(self,stri):
		if(stri.startswith("W")):
			new = list(stri)
			new[0] = "K"
			stri = ''.join(new)
			return stri
		elif(stri.startswith("B")):
			new = list(stri)
			new[0] = "Q"
			stri = ''.join(new)
			return stri
		else:
			pass
	
	#Driver function for white moves.
	def whiteDriver(self):		
		coordinate = raw_input("Please enter piece to move: ")
		direction = input("Which direction would you like to move? ")
		self.moveWhite(coordinate, direction)	
	
	#Function to move the white pieces, perform jumps and other input verification.
	#No king rules written in yet.	
	def moveWhite(self,str,move):

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

		#white movement could be split into functions still
		# needs to handle kings/queens
		#moving up and to the right
		if move == 9:

			#If moving out of right bound
			if((wval + 1) >= self.width):
				print (self.error.OutofBounds)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			# Wrong piece chosen; choose right piece.
			elif (str.startswith("B") | str.startswith("Q")):
				print(self.error.WrongPiece)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			#Default movement
			elif self.board[hval - 1][wval + 1] == "  ":
				self.board[hval - 1][wval + 1] = self.board[hval][wval]
				self.board[hval][wval] = "  "
				board.printboard()
				board.turn = "B"

			#If space is occupied by player piece
			elif(self.board[hval - 1][wval + 1].startswith("W") | self.board[hval - 1][wval + 1].startswith("K")):
				print(self.error.OccupiedSpace)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			#Instigate jump
			elif(self.board[hval - 1][wval + 1].startswith("B") | self.board[hval - 1][wval + 1].startswith("Q")):
				if(self.board[hval - 2][wval + 2].startswith("B") | self.board[hval - 2][wval + 2].startswith("Q")):
					print (self.error.OccupiedSpace)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					turn = "B"
				elif(self.board[hval - 2][wval + 2] == "  "):
					print (self.error.MustJump)
					self.board[hval - 2][wval + 2] = self.board[hval][wval]
					self.board[hval - 1][wval + 1] = "  "
					self.board[hval][wval] = " "
					board.printboard()
					board.turn = "B"
				elif((wval + 2) >= self.width):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

		# moving up and to the left
		elif move == 7:
			#If moving out of left bound
			if((wval - 1) < 0):
				print (self.error.OutofBounds)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			# Wrong piece chosen; choose right piece.
			elif (str.startswith("B") | str.startswith("Q")):
				print(self.error.WrongPiece)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			#Default movement
			elif self.board[hval - 1][wval - 1] == "  ":
				self.board[hval - 1][wval - 1] = self.board[hval][wval]
				self.board[hval][wval] = "  "
				board.printboard()
				board.turn = "B"

			#If space is occupied by player piece
			elif(self.board[hval - 1][wval - 1].startswith("W") | self.board[hval - 1][wval - 1].startswith("K")):
				print(self.error.OccupiedSpace)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			#Instigate jump
			elif(self.board[hval - 1][wval - 1].startswith("B") | self.board[hval - 1][wval - 1].startswith("Q")):
				if(self.board[hval - 2][wval - 2].startswith("B") | self.board[hval - 2][wval - 2].startswith("Q")):
					print (self.error.OccupiedSpace)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					turn = "B"
				elif(self.board[hval - 2][wval - 2] == "  "):
					print (self.error.MustJump)
					self.board[hval - 2][wval - 2] = self.board[hval][wval]
					self.board[hval - 1][wval - 1] = "  "
					self.board[hval][wval] = " "
					board.printboard()
					board.turn = "B"
				elif((wval - 2) < 0):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

		# kings moves and error handling for other moves
		elif move == 1:
			if str.startswith("W"):
				print (self.error.BackwardMove)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)

			# Wrong piece chosen; choose right piece.
			elif (str.startswith("B") | str.startswith("Q")):
				print(self.error.WrongPiece)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			#else it's a king
			else:
				if ((wval - 1) < 0) | (hval + 1 >= self.height):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# Default movement
				elif self.board[hval + 1][wval - 1] == "  ":
					self.board[hval + 1][wval - 1] = self.board[hval][wval]
					self.board[hval][wval] = "  "
					board.printboard()
					board.turn = "B"

				# If space is occupied by player piece
				elif (self.board[hval + 1][wval - 1].startswith("W") | self.board[hval + 1][wval - 1].startswith("K")):
					print(self.error.OccupiedSpace)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# Instigate jump
				elif (self.board[hval + 1][wval - 1].startswith("B") | self.board[hval + 1][wval - 1].startswith("Q")):
					if (self.board[hval + 2][wval - 2].startswith("B") | self.board[hval + 2][wval - 2].startswith("Q")):
						print (self.error.OccupiedSpace)
						coordinate = raw_input("Please enter piece to move: ")
						direction = input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						turn = "B"
					elif (self.board[hval + 2][wval - 2] == "  "):
						print (self.error.MustJump)
						self.board[hval + 2][wval - 2] = self.board[hval][wval]
						self.board[hval + 1][wval - 1] = "  "
						self.board[hval][wval] = " "
						board.printboard()
						board.turn = "B"
					elif ((wval - 2) < 0) | ((hval +2) >= self.height):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"

		elif move == 3:
			#if its a normal white piece move is illegal
			if str.startswith("W"):
				print (self.error.BackwardMove)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)

			# Wrong piece chosen; choose right piece.
			elif (str.startswith("B") | str.startswith("Q")):
				print(self.error.WrongPiece)
				coordinate = raw_input("Please enter piece to move: ")
				direction = input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)
				board.turn = "B"

			# else it's a king
			else:
				if ((wval + 1) < 0) | (hval + 1 >= self.height):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# Default movement
				elif self.board[hval + 1][wval + 1] == "  ":
					self.board[hval + 1][wval + 1] = self.board[hval][wval]
					self.board[hval][wval] = "  "
					board.printboard()
					board.turn = "B"

				# If space is occupied by player piece
				elif (self.board[hval + 1][wval + 1].startswith("W") | self.board[hval + 1][wval + 1].startswith("K")):
					print(self.error.OccupiedSpace)
					coordinate = raw_input("Please enter piece to move: ")
					direction = input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"
				# Instigate jump
				elif (self.board[hval + 1][wval + 1].startswith("B") | self.board[hval + 1][wval + 1].startswith("Q")):
					if (self.board[hval + 2][wval + 2].startswith("B") | self.board[hval + 2][wval + 2].startswith("Q")):
						print (self.error.OccupiedSpace)
						coordinate = raw_input("Please enter piece to move: ")
						direction = input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						turn = "B"
					elif (self.board[hval + 2][wval + 2] == "  "):
						print (self.error.MustJump)
						self.board[hval + 2][wval + 2] = self.board[hval][wval]
						self.board[hval + 1][wval + 1] = "  "
						self.board[hval][wval] = " "
						board.printboard()
						board.turn = "B"
					elif ((wval + 2) < 0) | ((hval + 2) >= self.height):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"
		else:
			print (self.error.InvalidMove)
			coordinate = raw_input("Please enter piece to move: ")
			direction = input("Which direction would you like to move? ")
			self.moveWhite(coordinate, direction)

		#get new location of the checker
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

		#make king if on top row
		if (hval == 0) & (str.startswith("K") == "False"):
			self.board[hval][wval] = self.kingme(str)
			self.printboard()

		
	def determinePieceToMoveEasy(self):
		#Looks through board state to find first piece with viable movement 
		i = 7
		j = 0
		wval = 0
		hval = 0
		while i >= 0:
			j = 0;
			while j < self.width:
				if self.board[i][j].startswith("B"):
					#Boundary checking for left side.					
					if((j - 1) < 0):
						if((self.board[i + 1][j + 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					#Boundary checking for right side.					
					if((j + 1) >= self.width):
						if((self.board[i + 1][j - 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j - 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					#Move left if a left move is available.
					elif((self.board[i + 1][j - 1] == "  ")):
						hval = i
						wval = j
						self.board[i + 1][j - 1] = self.board[hval][wval]
						self.board[hval][wval] = "  "
						self.printboard()
						board.turn = "W"
						return
					#If left space is occupied by white piece, and right move is available, move right.					
					elif(self.board[i + 1][j - 1].startswith("W")):
						if((self.board[i + 1][j + 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					#If right space is occupied, and left is available, move left.				
					elif(self.board[i + 1][j + 1].startswith("W")):
						if((self.board[i + 1][j - 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					#Create king piece for black.				
					if hval == 7:
						self.board[hval][wval] = self.kingme(str)
						self.printboard()
															
					
				j += 1
			i -= 1





#Easy mode module; will just examine black pieces, choose one that can perform valid move, and move it. No jumping.
#def easyMode(Board):
	 	

#Medium mode module: will move random black pieces, but can jump the player.
#class mediumMode():

#Hard mode class: use heuristic search to determine best move based on available user and computer moves; can and will jump.
#class hardMode():
	



#start of main function area
#build a board that is 8x8, place checkers and print it out
board = Board(8, 8)
board.setup()
board.printboard()
iter1 = 0
board.printboard()
while(iter1 <= 15):
	board.whiteDriver()
	board.determinePieceToMoveEasy()
	iter1 += 1

	
