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
	InvalidPiece = "That Piece does not exist, pieces are of the form Aa"
	OccupiedSpace = "Player must move to an empty space."
	MoveTooLong = "Player must move exactly two spaces."
	BackwardMove = "Only king can move backward."
	MustJump = "Player must jump opponent in this move, and must do multiple jumps, if possible."
	KingPiece = "Move terminates immediately if piece enters king's row."
	JumpMove = "If a move starts with a jump, only jumps can be performed."
	InvalidCapture = "Player can only capture opponent's pieces."
	InvalidMove = "Please move to an adjacent empty space, or jump the opponent."
	OutofBounds = "That move is out of bounds. Please choose another move."
	InvalidInput = "You can move pieces with 7 and 9 (or 1 and 3 as well for kings). Please give valid input."


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
		wnum = 0
		bnum = 0
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
			return stri
	
	#Driver function for white moves.
	def whiteDriver(self):		
		coordinate = raw_input("Please enter piece to move: ")
		direction = raw_input("Which direction would you like to move? ")
		self.moveWhite(coordinate, direction)	
	
	#Function to move the white pieces, perform jumps and other input verification.
	#No king rules written in yet.	
	def moveWhite(self,str,move):

		#find the location of the checker we are looking for, could be a function
		#that returns to a checkers class with wval, hval, and str for variables?
		i = 0
		j = 0
		found = 0
		wval = 0
		hval = 0
		while i < self.height:
			j = 0
			while j < self.width:
				if self.board[i][j] == str:
					hval = i
					wval = j
					found = 1
				j += 1
			i += 1
		if found == 0:
			print (self.error.InvalidPiece)
			coordinate = raw_input("Please enter piece to move: ")
			direction = raw_input("Which direction would you like to move? ")
			self.moveWhite(coordinate, direction)
			board.turn = "B"

			
		elif found == 1:

			# If moving up and to right
			if move == '9':

				# If moving out of right bound
				if ((wval + 1) >= self.width) | ((hval - 1) < 0):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# Wrong piece chosen; choose right piece.
				elif (str.startswith("B") | str.startswith("Q")):
					print(self.error.WrongPiece)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
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
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				#Instigate jump
				elif(self.board[hval - 1][wval + 1].startswith("B") | self.board[hval - 1][wval + 1].startswith("Q")):
					if ((wval + 2) >= self.width) | ((hval - 2) < 0):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"
					elif(self.board[hval - 2][wval + 2].startswith("B") | self.board[hval - 2][wval + 2].startswith("Q")):
						print (self.error.OccupiedSpace)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						turn = "B"
					elif(self.board[hval - 2][wval + 2] == "  "):
						print (self.error.MustJump)
						self.board[hval - 2][wval + 2] = self.board[hval][wval]
						self.board[hval - 1][wval + 1] = "  "
						self.board[hval][wval] = "  "
						board.blackPieces -= 1
						board.printboard()
						board.turn = "B"

			# moving up and to the left
			elif move == '7':
				#If moving out of left bound
				if(wval - 1) < 0 | (hval - 1 < 0):
					print (self.error.OutofBounds)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# Wrong piece chosen; choose right piece.
				elif (str.startswith("B") | str.startswith("Q")):
					print(self.error.WrongPiece)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
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
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				#Instigate jump
				elif(self.board[hval - 1][wval - 1].startswith("B") | self.board[hval - 1][wval - 1].startswith("Q")):
					if ((wval - 2) < 0) | ((hval - 2) < 0):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"
					elif(self.board[hval - 2][wval - 2].startswith("B") | self.board[hval - 2][wval - 2].startswith("Q")):
						print (self.error.OccupiedSpace)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						turn = "B"
					elif(self.board[hval - 2][wval - 2] == "  "):
						print (self.error.MustJump)
						self.board[hval - 2][wval - 2] = self.board[hval][wval]
						self.board[hval - 1][wval - 1] = "  "
						self.board[hval][wval] = "  "
						board.blackPieces -= 1
						board.printboard()
						board.turn = "B"

			# kings moves and error handling for other moves
			elif move == '1':
				if str.startswith("W"):
					print (self.error.BackwardMove)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)

				# Wrong piece chosen; choose right piece.
				elif (str.startswith("B") | str.startswith("Q")):
					print(self.error.WrongPiece)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				#else it's a king
				else:
					if ((wval - 1) < 0) | (hval + 1 >= self.height):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
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
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"

					# Instigate jump
					elif (self.board[hval + 1][wval - 1].startswith("B") | self.board[hval + 1][wval - 1].startswith("Q")):
						if ((wval - 2) < 0) | ((hval + 2) >= self.height):
							print (self.error.OutofBounds)
							coordinate = raw_input("Please enter piece to move: ")
							direction = raw_input("Which direction would you like to move? ")
							self.moveWhite(coordinate, direction)
							board.turn = "B"
						elif (self.board[hval + 2][wval - 2].startswith("B") | self.board[hval + 2][wval - 2].startswith("Q")):
							print (self.error.OccupiedSpace)
							coordinate = raw_input("Please enter piece to move: ")
							direction = raw_input("Which direction would you like to move? ")
							self.moveWhite(coordinate, direction)
							turn = "B"
						elif (self.board[hval + 2][wval - 2] == "  "):
							print (self.error.MustJump)
							self.board[hval + 2][wval - 2] = self.board[hval][wval]
							self.board[hval + 1][wval - 1] = "  "
							self.board[hval][wval] = "  "
							board.blackPieces -= 1
							board.printboard()
							board.turn = "B"


			elif move == '3':
				#if its a normal white piece move is illegal
				if str.startswith("W"):
					print (self.error.BackwardMove)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)

				# Wrong piece chosen; choose right piece.
				elif (str.startswith("B") | str.startswith("Q")):
					print(self.error.WrongPiece)
					coordinate = raw_input("Please enter piece to move: ")
					direction = raw_input("Which direction would you like to move? ")
					self.moveWhite(coordinate, direction)
					board.turn = "B"

				# else it's a king
				else:
					if (((wval + 1) >= self.width) | (hval + 1 >= self.height)):
						print (self.error.OutofBounds)
						coordinate = raw_input("Please enter piece to move: ")
						direction = raw_input("Which direction would you like to move? ")
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
						direction = raw_input("Which direction would you like to move? ")
						self.moveWhite(coordinate, direction)
						board.turn = "B"
					# Instigate jump
					elif (self.board[hval + 1][wval + 1].startswith("B") | self.board[hval + 1][wval + 1].startswith("Q")):
						if ((wval + 2) >= self.width) | ((hval + 2) >= self.height):
							print (self.error.OutofBounds)
							coordinate = raw_input("Please enter piece to move: ")
							direction = raw_input("Which direction would you like to move? ")
							self.moveWhite(coordinate, direction)
							board.turn = "B"
						elif (self.board[hval + 2][wval + 2].startswith("B") | self.board[hval + 2][wval + 2].startswith("Q")):
							print (self.error.OccupiedSpace)
							coordinate = raw_input("Please enter piece to move: ")
							direction = raw_input("Which direction would you like to move? ")
							self.moveWhite(coordinate, direction)
							turn = "B"
						elif (self.board[hval + 2][wval + 2] == "  "):
							print (self.error.MustJump)
							self.board[hval + 2][wval + 2] = self.board[hval][wval]
							self.board[hval + 1][wval + 1] = "  "
							self.board[hval][wval] = "  "
							board.blackPieces -= 1
							board.printboard()
							board.turn = "B"

			else:
				print (self.error.InvalidInput)
				coordinate = raw_input("Please enter piece to move: ")
				direction = raw_input("Which direction would you like to move? ")
				self.moveWhite(coordinate, direction)

			#get new location of the checker
			i = 0
			j = 0
			wval = 0
			hval = 0
			while i < self.height:
				j = 0
				while j < self.width:
					if self.board[i][j] == str:
						hval = i
						wval = j
					j += 1
				i += 1

			#make king if on top row
			if (hval == 0):
				self.board[hval][wval] = self.kingme(str)
				self.printboard()

		
	def beginnerMode(self):
		#Looks through board state to find first piece with viable movement 
		i = 7
		j = 0
		wval = 0
		hval = 0
		while i >= 0:
			j = 0;
			while j < self.width:
				if self.board[i][j].startswith("B"):
					#If at end of board, black wins.
					if(i + 1 >= self.height):
						board.whitePieces = 0
						return					
					#Boundary checking for left side.					
					if((j - 1) < 0):
						#If right space is available to take, move  there.						
						if((self.board[i + 1][j + 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
						#Else, move onto next piece to be checked			
						elif(self.board[i + 1][j + 1].startswith("W")):
							j += 1
							continue
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
						#Else, move onto next piece to be checked			
						elif(self.board[i + 1][j - 1].startswith("W")):
							j += 1
							continue
					if(i + 1 < self.height and j - 1 >= 0):
						#Move left if a left move is available.
						if((self.board[i + 1][j - 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j - 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					if(i + 1 < self.height and j + 1 < self.width):					
						#Else if right move is available.					
						if((self.board[i + 1][j + 1] == "  ")):
							hval = i
							wval = j
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
					#If left space is occupied by white piece or black piece, and right move is available, move right.					
					elif(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("B")):
						if(i + 1 < self.height and j + 1 < self.width):
							if((self.board[i + 1][j + 1] == "  ")):
								hval = i
								wval = j
								self.board[i + 1][j + 1] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.printboard()
								board.turn = "W"
								return
							else:
								break

					#If right space is occupied, and left is available, move to next piece				
					elif(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("B")):
						if(i + 1 < self.height and (j - 1) >= 0):
							if(self.board[i + 1][j - 1] == "  "):
								hval = i
								wval = j
								self.board[i + 1][j + 1] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.printboard()
								board.turn = "W"
								return					
					else:
						return
																		
				j += 1
			i -= 1


	#Function to determine if a jump is immediately available.
	def jumpCheck(self):
		i = 7
		j = 0
		wval = 0
		hval = 0
		
		while i >= 0:
			j = 0;
			while j < self.width:
				if(self.board[i][j].startswith("B") or self.board[i][j].startswith("Q")):
					#Boundary checking for left side.					
					if((j - 1) < 0):
						#Boundary check for bottom right.
						if(i + 1 < self.height and j + 1 < self.width):						
							#If space occupied by player piece, check for available jump.			
							if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
								if((self.board[i + 2][j + 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])								
									self.board[i + 2][j + 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j + 1] = "  "
									board.whitePieces -= 1									
									self.printboard()
									board.turn = "W"
									return 1
					#Boundary checking for right side.					
					if((j + 1) >= self.width):
						#Boundary checking for bottom left.
						if(i + 1 < self.height and j - 1 <= 0):						
							#If space occupied by player piece, check for available jump.
							if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
								if((self.board[i + 2][j - 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])								
									self.board[i + 2][j - 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j - 1] = "  "
									board.whitePieces -= 1									
									self.printboard()
									board.turn = "W"
									return 1
					if(((j - 1) != -1) and (i + 1 != 8)):					
						#If left space is occupied, and a jump is available, take the jump.				
						if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
							#Boundary checking for left jump; if out of range, check right move.
							if(i + 2 < self.height and j - 2 < 0):
								#If a jump is available to the right, check for valid move.
								if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):									
									if((self.board[i + 2][j + 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])										
										self.board[i + 2][j + 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j + 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return 1						
							
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i + 1][j + 1].startswith("B") or self.board[i + 1][j + 1].startswith("Q")):
									j += 1
									continue
								
							#Else if move is valid, make jump.						
							if((not(i + 2) >= self.height) and (not(j - 2) < 0)):							
								if((self.board[i + 2][j - 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 2][j - 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j - 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return 1
					if((j + 1 != self.width) and (i + 1 != 8)):					
						#If right space is occupied, and a jump is available, take the jump.				
						if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
							#Boundary checking for right jump; if out of range, check left move.
							if(i + 2 < self.height and j + 2 >= self.width):
								#If a jump is available to the left, check for valid move.
								if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
									if((self.board[i + 2][j - 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])										
										self.board[i + 2][j - 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j - 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return 1
							
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i + 1][j - 1].startswith("B") or self.board[i + 1][j - 1].startswith("Q")):
									j += 1
									continue						
							#Else if within range, check for jump.						
							if((not(i + 2) >= self.height) and (not(j + 2) >= self.width)):							
								if((self.board[i + 2][j + 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 2][j + 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j + 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return 1
					
					#Movement abilities for Queens only 
					if(self.board[i][j].startswith("Q")):
						#If left space is occupied, and a jump is available, take the jump.				
						if(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):						
							#Boundary checking for left up jump; if out of range, check right move.
							if(i - 2 < 0 or j - 2 < 0):
								#Else if a jump is available to the right, check for valid move.
								if(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
									if((self.board[i - 2][j + 2] == "  ")):
										hval = i
										wval = j
										self.board[i - 2][j + 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i - 1][j + 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return 1
						
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i - 1][j + 1].startswith("B") or self.board[i - 1][j + 1].startswith("Q") ):
									j += 1
									continue
							
							#Else if move is valid, make jump.						
							elif((self.board[i - 2][j - 2] == "  ")):
								hval = i
								wval = j
								self.board[i - 2][j - 2] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.board[i - 1][j - 1] = "  "
								board.whitePieces -= 1							
								self.printboard()
								board.turn = "W"
								return	1
					
						#If right up space is occupied, and a jump is available, take the jump.				
						elif(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
							#Boundary checking for right up jump; if out of range, check left move.
							if(j + 2 >= self.width):
								if((self.board[i - 1][j - 1] == "  ")):
									hval = i
									wval = j
									self.board[i - 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return 1
						
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i - 1][j - 1].startswith("B") or self.board[i - 1][j - 1].startswith("Q")):
									j += 1
									continue
								#Else if a jump is available to the left, check for valid move.
								elif(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):
									if((self.board[i - 2][j - 2] == "  ")):
										hval = i
										wval = j
										self.board[i - 2][j - 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i - 1][j - 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return 1
							#Else if move is valid, make jump.						
							elif((self.board[i - 2][j + 2] == "  ")):
								hval = i
								wval = j
								self.board[i - 2][j + 2] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.board[i - 1][j + 1] = "  "
								board.whitePieces -= 1							
								self.printboard()
								board.turn = "W"
								return 1

				j += 1			
			i -= 1
		return 0	
					

	def mediumMode(self):
		#Looks through board state to find first piece with viable movement 
		i = 7
		j = 0
		wval = 0
		hval = 0
		while i >= 0:
			j = 0;
			while j < self.width:
				if self.board[i][j].startswith("B") or self.board[i][j].startswith("Q"):
					jumpCheck = self.jumpCheck()
					if(jumpCheck == 1):
						return			
					else:											
						#Boundary checking for left side.					
						if((j - 1) < 0):
							#If right move is available, take it.						
							if((self.board[i + 1][j + 1] == "  ")):
								hval = i
								wval = j
								#Create queen piece for black.				
								if hval + 1 == 7:
									self.board[hval][wval] = self.kingme(self.board[hval][wval])								
								self.board[i + 1][j + 1] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.printboard()
								board.turn = "W"
								return
							#Else, if space occupied by player piece, check for available jump.			
							elif(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
								if(i + 2 < self.height):								
									if((self.board[i + 2][j + 2] == "  ")):
											hval = i
											wval = j
											#Create queen piece for black.				
											if hval + 2 == 7:
												self.board[hval][wval] = self.kingme(self.board[hval][wval])
											self.board[i + 2][j + 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j + 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
							elif(self.board[i + 1][j + 1].startswith("B") or self.board[i + 1][j + 1].startswith("Q")):
								j += 1
								continue
						#Boundary checking for right side.					
						if((j + 1) >= self.width):
							#If Left space is open, move there.						
							if((self.board[i + 1][j - 1] == "  ")):
								hval = i
								wval = j
								#Create queen piece for black.				
								if hval + 1 == 7:
									self.board[hval][wval] = self.kingme(self.board[hval][wval])								
								self.board[i + 1][j - 1] = self.board[hval][wval]
								self.board[hval][wval] = "  "
								self.printboard()
								board.turn = "W"
								return
							#Else, if space occupied by player piece, check for available jump.
							elif(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
								if(i + 2 < self.height):								
									if((self.board[i + 2][j - 2] == "  ")):
											hval = i
											wval = j
											#Create queen piece for black.				
											if hval + 2 == 7:
												self.board[hval][wval] = self.kingme(self.board[hval][wval])                                                                   
											self.board[i + 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
							elif(self.board[i + 1][j - 1].startswith("B") or self.board[i + 1][j - 1].startswith("Q")):
								j += 1
								continue
						#If left space is occupied, and a jump is available, take the jump.										
						if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
							#Boundary checking for left jump; if out of range, check right move.
							if(i + 2 < self.height and j - 2 < 0):
								#If a jump is available to the right, check for valid move.
								if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
									if((self.board[i + 2][j + 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval  + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])										
										self.board[i + 2][j + 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j + 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return								
								elif((self.board[i + 1][j + 1] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 1][j + 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "								
									self.printboard()
									board.turn = "W"
									return	
						
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i + 1][j + 1].startswith("B") or self.board[i + 1][j + 1].startswith("Q")):
									j += 1
									continue
							elif((not(i + 2) >= self.height) and (not(j - 2) < 0)):							
								#Else if move is valid, make jump.						
								if((self.board[i + 2][j - 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 2][j - 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j - 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return									
						#If right space is occupied, and a jump is available, take the jump.				
						if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
							#Boundary checking for right jump; if out of range, check left move.
							if(i + 2 < self.height and j + 2 >= self.width):
								#If a jump is available to the left, check for valid move.
								if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("W")):
									if((self.board[i + 2][j - 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])											
										self.board[i + 2][j - 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j - 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return								
								elif((self.board[i + 1][j - 1] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return	
							
								#Else if space is taken by black piece, move to next piece for analysis.
								elif(self.board[i + 1][j - 1].startswith("B") or self.board[i + 1][j - 1].startswith("Q")):
									j += 1
									continue
							elif((not(i + 2) >= self.height) and (not(j + 2) >= self.width)):
								#Else if move is valid, make jump.						
								if((self.board[i + 2][j + 2] == "  ")):
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 2 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])									
									self.board[i + 2][j + 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i + 1][j + 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return	

						#Else move left if a left move is available.
						elif((self.board[i + 1][j - 1] == "  ")):
							hval = i
							wval = j
							#Create queen piece for black.				
							if hval + 1 == 7:
								self.board[hval][wval] = self.kingme(self.board[hval][wval])							
							self.board[i + 1][j - 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return
						#Else if move right if a right move is available.
						elif((self.board[i + 1][j + 1] == "  ")):
							hval = i
							wval = j
							#Create queen piece for black.				
							if hval + 1 == 7:
								self.board[hval][wval] = self.kingme(self.board[hval][wval])							
							self.board[i + 1][j + 1] = self.board[hval][wval]
							self.board[hval][wval] = "  "
							self.printboard()
							board.turn = "W"
							return	

						#Boundary checking for Queens
						if(self.board[i][j].startswith("Q")):
							#Boundary check for bottom of board
							if((i + 1) >= self.height):
								#If Left space is open, move there.						
								if((self.board[i - 1][j - 1] == "  ")):
									check = board.checkMove(i - 1, j - 1)
									if(check == 1):							
										hval = i
										wval = j
										self.board[i - 1][j - 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return
									elif(check == 0):									
										pass
								#Else, if space occupied by player piece, check for available jump.
								elif(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("W")):
									if((self.board[i - 2][j - 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return					
							#Boundary check for top of board
							if((i - 1) < 0):
								#If up right move is available, take it.						
								if((self.board[i + 1][j + 1] == "  ")):
									check = board.checkMove(i + 1, j + 1)							
									if(check == 1):							
										hval = i
										wval = j
										self.board[i + 1][j + 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return
									elif(check == 0):
										pass
								#Else, if space occupied by player piece, check for available jump.			
								elif(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
									if((self.board[i + 2][j + 2] == "  ")):
											hval = i
											wval = j
											self.board[i + 2][j + 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j + 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return

						#Movement abilities for Queens only 
						if(self.board[i][j].startswith("Q")):
							#If left space is occupied, and a jump is available, take the jump.				
							if(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):						
								#Boundary checking for left up jump; if out of range, check right move.
								if(i - 2 < 0 or j - 2 < 0):
									#Else if a jump is available to the right, check for valid move.
									if(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
										if((self.board[i - 2][j + 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j + 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j + 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
									elif((self.board[i - 1][j + 1] == "  ")):								
										hval = i
										wval = j
										self.board[i - 1][j + 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "								
										self.printboard()
										board.turn = "W"
										return	
							
									#Else if space is taken by black piece or queen, move to next piece for analysis.
									elif(self.board[i - 1][j + 1].startswith("B") or self.board[i - 1][j + 1].startswith("Q")):
										j += 1
										continue
								
								#Else if move is valid, make jump.						
								elif((self.board[i - 2][j - 2] == "  ")):
									hval = i
									wval = j
									self.board[i - 2][j - 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i - 1][j - 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return	
						
							#If right up space is occupied, and a jump is available, take the jump.				
							elif(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
								#Boundary checking for right up jump; if out of range, check left move.
								if(j + 2 >= self.width):
									if((self.board[i - 1][j - 1] == "  ")):
										hval = i
										wval = j
										self.board[i - 1][j - 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return	
							
									#Else if space is taken by black piece or queen, move to next piece for analysis.
									elif(self.board[i - 1][j - 1].startswith("B") or self.board[i - 1][j - 1].startswith("Q")):
										j += 1
										continue
									#Else if a jump is available to the left, check for valid move.
									elif(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):
										if((self.board[i - 2][j - 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
								#Else if move is valid, make jump.						
								elif((self.board[i - 2][j + 2] == "  ")):
									hval = i
									wval = j
									self.board[i - 2][j + 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i - 1][j + 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return	

							#Else move up left if a left move is available.
							elif((self.board[i - 1][j - 1] == "  ")):					
									hval = i
									wval = j
									self.board[i - 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								
							#Else if move up right if a right move is available.
							elif((self.board[i - 1][j + 1] == "  ")):
														
									hval = i
									wval = j
									self.board[i - 1][j + 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return									
					
				j += 1
			i -= 1
		
	 	

	def checkMove(self, hval, wval):
		if(self.board[hval][wval] == "  "):
			pass		
		else:
			return 0

		if((wval == 0) or (hval == 0) or (wval == self.width-1) or (hval == self.height -1)):
			return 1
		
		if(self.board[hval + 1][wval - 1].startswith("W") == False and self.board[hval + 1][wval - 1].startswith("K") == False):
			pass
		else:	
			return 0

		if(self.board[hval + 1][wval +1 ].startswith("W") == False and self.board[hval + 1][wval + 1].startswith("K") == False):
			pass
		else:
			return 0
		
		if(self.board[hval - 1][wval - 1].startswith("K") == False):
			pass
		else:
			return 0
		
		if(self.board[hval - 1][wval + 1].startswith("K") == False):
			return 1
		
		else:
			return 0

		if(self.board[hval - 1][wval + 1] != "  " and self.board[hval + 1][wval - 1] != "  "):
			return 1
		else:	
			return 0

		
		
		

	def hardMode(self):
		#Looks through board state to find first piece with viable movement 
		i = 7
		j = 0
		wval = 0
		hval = 0
		
		while i >= 0:
			j = 0;
			while j < self.width:				
				if self.board[i][j].startswith("B") or self.board[i][j].startswith("Q"):
					jumpCheck = self.jumpCheck() 
					if(jumpCheck == 1):
						return			
					else:											
						#Boundary checking for left side.					
						if((j - 1) < 0):
							#If right move is available, take it.						
							if((self.board[i + 1][j + 1] == "  ")):
								check = board.checkMove(i + 1, j + 1)									
								if(check == 1):														
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])								
									self.board[i + 1][j + 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "								
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):									
									j += 1
									continue
							#Else, if space occupied by player piece, check for available jump.			
							elif(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
								if((self.board[i + 2][j + 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])
										self.board[i + 2][j + 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j + 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return
							elif(self.board[i + 1][j + 1].startswith("B") or self.board[i + 1][j + 1].startswith("Q")):
								j += 1
								continue
						#Boundary checking for right side.					
						if((j + 1) >= self.width):
							#If Left space is open, move there.						
							if((self.board[i + 1][j - 1] == "  ")):
								check = board.checkMove(i + 1, j - 1)
								if(check == 1):								
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])								
									self.board[i + 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):
									self.forceMove = 1
									pass
							#Else, if space occupied by player piece, check for available jump.
							elif(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
								if((self.board[i + 2][j - 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])                                                                   
										self.board[i + 2][j - 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j - 1] = "  "
										board.whitePieces -= 1									
										self.printboard()
										board.turn = "W"
										return
							elif(self.board[i + 1][j - 1].startswith("B")):
								j += 1
								continue
						
						#Boundary checking for Queens
						if(self.board[i][j].startswith("Q")):
							#Boundary check for bottom of board
							if((i + 1) >= self.height):
								#If Left space is open, move there.						
								if((self.board[i - 1][j - 1] == "  ")):
									check = board.checkMove(i - 1, j - 1)
									if(check == 1):							
										hval = i
										wval = j
										self.board[i - 1][j - 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return
									elif(check == 0):									
										pass
								#Else, if space occupied by player piece, check for available jump.
								elif(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("W")):
									if((self.board[i - 2][j - 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return					
							#Boundary check for top of board
							if((i - 1) < 0):
								#If up right move is available, take it.						
								if((self.board[i + 1][j + 1] == "  ")):
									check = board.checkMove(i + 1, j + 1)							
									if(check == 1):							
										hval = i
										wval = j
										self.board[i + 1][j + 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return
									elif(check == 0):
										pass
								#Else, if space occupied by player piece, check for available jump.			
								elif(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
									if((self.board[i + 2][j + 2] == "  ")):
											hval = i
											wval = j
											self.board[i + 2][j + 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j + 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
						#Boundary  check
						if(i + 1 < self.height and j - 1 < 0):
								#If left space is occupied, and a jump is available, take the jump.				
								if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("K")):
									#Boundary checking for left jump; if out of range, check right move.
									if(i + 2 < self.height and j - 2 < 0):
										#If a jump is available to the right, check for valid move.
										if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
											if((self.board[i + 2][j + 2] == "  ")):
												hval = i
												wval = j
												#Create queen piece for black.				
												if hval  + 2 == 7:
													self.board[hval][wval] = self.kingme(self.board[hval][wval])										
												self.board[i + 2][j + 2] = self.board[hval][wval]
												self.board[hval][wval] = "  "
												self.board[i + 1][j + 1] = "  "
												board.whitePieces -= 1									
												self.printboard()
												board.turn = "W"
												return								
										elif((self.board[i + 1][j + 1] == "  ")):
											hval = i
											wval = j
											#Create queen piece for black.				
											if hval + 1 == 7:
												self.board[hval][wval] = self.kingme(self.board[hval][wval])									
											self.board[i + 1][j + 1] = self.board[hval][wval]
											self.board[hval][wval] = "  "								
											self.printboard()
											board.turn = "W"
											return	
						
										#Else if space is taken by black piece, move to next piece for analysis.
										elif(self.board[i + 1][j + 1].startswith("B")):
											j += 1
											continue
									elif((not(i + 2) >= self.height) and (not(j - 2) < 0)):							
										#Else if move is valid, make jump.						
										if((self.board[i + 2][j - 2] == "  ")):
											hval = i
											wval = j
											#Create queen piece for black.				
											if hval + 2 == 7:
												self.board[hval][wval] = self.kingme(self.board[hval][wval])									
											self.board[i + 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j - 1] = "  "
											board.whitePieces -= 1							
											self.printboard()
											board.turn = "W"
											return									
						
						#Boundary check.						
						if(i + 1 < self.height and j + 1 < self.width):						
							#If right space is occupied, and a jump is available, take the jump.				
							if(self.board[i + 1][j + 1].startswith("W") or self.board[i + 1][j + 1].startswith("K")):
								#Boundary checking for right jump; if out of range, check left move.
								if(i + 2 < self.height and j + 2 >= self.width):
									#If a jump is available to the left, check for valid move.
									if(self.board[i + 1][j - 1].startswith("W") or self.board[i + 1][j - 1].startswith("W")):
										if((self.board[i + 2][j - 2] == "  ")):
											hval = i
											wval = j
											#Create queen piece for black.				
											if hval + 2 == 7:
												self.board[hval][wval] = self.kingme(self.board[hval][wval])											
											self.board[i + 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i + 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return								
									elif((self.board[i + 1][j - 1] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 1 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])									
										self.board[i + 1][j - 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return	
							
									#Else if space is taken by black piece, move to next piece for analysis.
									elif(self.board[i + 1][j - 1].startswith("B")):
										j += 1
										continue
								elif((not(i + 2) >= self.height) and (not(j + 2) >= self.width)):
									#Else if move is valid, make jump.						
									if((self.board[i + 2][j + 2] == "  ")):
										hval = i
										wval = j
										#Create queen piece for black.				
										if hval + 2 == 7:
											self.board[hval][wval] = self.kingme(self.board[hval][wval])									
										self.board[i + 2][j + 2] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.board[i + 1][j + 1] = "  "
										board.whitePieces -= 1							
										self.printboard()
										board.turn = "W"
										return	
						#Boundary checking
						if(i + 1 < self.height and j - 1 >= 0):
							#Else move left if a left move is available.
							if((self.board[i + 1][j - 1] == "  ")):
								check = board.checkMove(i + 1, j - 1)
								if(check == 1):							
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])							
									self.board[i + 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):
									pass
						#Boundary checking right move.
						elif(i + 1 < self.height and j + 1 < self.width):						
							#Else if move right if a right move is available.
							if((self.board[i + 1][j + 1] == "  ")):
								check = board.checkMove(i + 1, j - 1)
								if(check == 1):							
									hval = i
									wval = j
									#Create queen piece for black.				
									if hval + 1 == 7:
										self.board[hval][wval] = self.kingme(self.board[hval][wval])							
									self.board[i + 1][j + 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):
									pass

						#Movement abilities for Queens only 
						if(self.board[i][j].startswith("Q")):
							#If left space is occupied, and a jump is available, take the jump.				
							if(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):						
								#Boundary checking for left up jump; if out of range, check right move.
								if(i - 2 < 0 or j - 2 < 0):
									#Else if a jump is available to the right, check for valid move.
									if(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
										if((self.board[i - 2][j + 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j + 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j + 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
									elif((self.board[i - 1][j + 1] == "  ")):								
										hval = i
										wval = j
										self.board[i - 1][j + 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "								
										self.printboard()
										board.turn = "W"
										return	
							
									#Else if space is taken by black piece, move to next piece for analysis.
									elif(self.board[i - 1][j + 1].startswith("B")):
										j += 1
										continue
								
								#Else if move is valid, make jump.						
								elif((self.board[i - 2][j - 2] == "  ")):
									hval = i
									wval = j
									self.board[i - 2][j - 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i - 1][j - 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return	
						
							#If right up space is occupied, and a jump is available, take the jump.				
							elif(self.board[i - 1][j + 1].startswith("W") or self.board[i - 1][j + 1].startswith("K")):
								#Boundary checking for right up jump; if out of range, check left move.
								if(j + 2 >= self.width):
									if((self.board[i - 1][j - 1] == "  ")):
										hval = i
										wval = j
										self.board[i - 1][j - 1] = self.board[hval][wval]
										self.board[hval][wval] = "  "
										self.printboard()
										board.turn = "W"
										return	
							
									#Else if space is taken by black piece, move to next piece for analysis.
									elif(self.board[i - 1][j - 1].startswith("B")):
										j += 1
										continue
									#Else if a jump is available to the left, check for valid move.
									elif(self.board[i - 1][j - 1].startswith("W") or self.board[i - 1][j - 1].startswith("K")):
										if((self.board[i - 2][j - 2] == "  ")):
											hval = i
											wval = j
											self.board[i - 2][j - 2] = self.board[hval][wval]
											self.board[hval][wval] = "  "
											self.board[i - 1][j - 1] = "  "
											board.whitePieces -= 1									
											self.printboard()
											board.turn = "W"
											return
								#Else if move is valid, make jump.						
								elif((self.board[i - 2][j + 2] == "  ")):
									hval = i
									wval = j
									self.board[i - 2][j + 2] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.board[i - 1][j + 1] = "  "
									board.whitePieces -= 1							
									self.printboard()
									board.turn = "W"
									return	

							#Else move up left if a left move is available.
							elif((self.board[i - 1][j - 1] == "  ")):
								check = board.checkMove(i - 1, j - 1)
								if(check == 1):						
									hval = i
									wval = j
									self.board[i - 1][j - 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):
									pass
								
							#Else if move up right if a right move is available.
							elif((self.board[i - 1][j + 1] == "  ")):
								check = board.checkMove(i - 1, j + 1)
								if(check == 1):						
									hval = i
									wval = j
									self.board[i - 1][j + 1] = self.board[hval][wval]
									self.board[hval][wval] = "  "
									self.printboard()
									board.turn = "W"
									return
								elif(check == 0):
									pass									
					
				j += 1
			i -= 1		
		board.mediumMode()
		
		
	



#start of main function area
#build a board that is 8x8, place checkers and print it out
board = Board(8, 8)
board.setup()

gameChoice = 'Y'

while(gameChoice == 'Y'):

	board.blackPieces = 12
	board.whitePieces = 12	

	mode = raw_input("Which mode would you like to play? Beginner(B), Medium(M), or Hard(H)? ")

	while(mode != "Beginner" and  mode != "B" and  mode != "b" and  mode != "Medium" and  mode != "M" and  mode != "m" and  mode != "Hard" and  mode != "H" and  mode != "h"):
		mode = raw_input("Please type in a valid option: ")

	if (mode == "Beginner" or mode == 'B' or mode == 'b'):
		board.printboard()	
		while(board.blackPieces != 0 and board.whitePieces != 0):
			if(board.turn == "W"):
				board.whiteDriver()
			elif(board.turn == "B"):
				board.beginnerMode()
	
		if(board.blackPieces == 0):
			print "White wins!"
		elif(board.whitePieces == 0):
			print "Black got to the end! Black wins!"

	elif(mode == "Medium" or mode == "M" or mode == "m"):
		board.printboard()
		while(board.blackPieces != 0 and board.whitePieces != 0):
			if(board.turn == "W"):
				board.whiteDriver()
			elif(board.turn == "B"):
				board.mediumMode()

		if(board.blackPieces == 0):	
			print "White wins!"
		elif(board.whitePieces == 0):
			print "Black wins!"

	elif(mode == "Hard" or mode == "H" or mode == "h"):
		board.printboard()
		while(board.blackPieces != 0 and board.whitePieces != 0):
			if(board.turn == "W"):
				board.whiteDriver()
			elif(board.turn == "B"):
				board.hardMode()

		if(board.blackPieces == 0):	
			print "White wins!"
		elif(board.whitePieces == 0):
			print "Black wins!"

	gameChoice = raw_input("Would you like to play again? (Y/N) ")
	
	while(gameChoice != 'Y' and gameChoice != 'y' and gameChoice != 'N' and gameChoice != 'n'):
		gameChoice = raw_input("Please type in a valid option: ")
