#!/usr/bin/env python

#INPUT 
#grid_list:  list of zeros and hypens
#piece_list: for default orientation, grid squares filled by a piece
#
#CONTENTS
#grid: array of array of strings. 0 = empty, - = not usable,
#pieces: array of the pieces valid for this board
#will be filled with piece ids over time
#xy_next: [x,y] where placing first piece not in use
#orient_next: int[0-3] with 0 up, 1 right, etc to orient piece
#placing_piece: location in array of piece being placed at this call level
class Board:
	def __init__(self,grid_list = [], piece_list = [], *args):
		self.xy_next = [0,0]
		self.placing_piece = 0
		self.grid = [list(line) for line in grid_list]

		if len(piece_list) > 100:
			raise(AssertionError, "Weird stuff is going to happen with your chars")

		self.pieces = []
		char_num = 65 #ASCII 'A' - want lot of readable chars in a row
		for line in piece_list:
			self.pieces.append(Piece(line,char_num))
			char_num += 1

	def __repr__(self):
		return "Grid: " + str(self.grid) + \
		"\nPieces: " + str(self.pieces) + \
		"\nxy_next: " + str(self.xy_next) + \
		"\nplacing piece:" + str(self.placing_piece)

	#how wide and long is the valid placing area
	def valid_bounds(self):
		return [len(self.grid[0]),len(self.grid)]

	def in_bounds_test(self):
		return (self.xy_next[0] < self.valid_bounds()[0] and self.xy_next[1] < self.valid_bounds()[1])

	#ADD ONCE MINI LOOP TESTED
	def valid_placement_test(self):
		return True

	#not smart. will overflow bounds
	def advance_next_placement(self):
		x = self.xy_next[0]
		if x < (self.valid_bounds()[0] - 1):
			self.xy_next[0] += 1
		else:
			self.xy_next[0] = 0
			self.xy_next[1] += 1

	#returns either a board or False. Recursive.
	def attempt_solve(self):
		if (self.placing_piece > len(self.pieces)):
			return self
		#while still possibilities left to try for placing_piece
		while (self.in_bounds_test()):
			#self.pieces[placing_piece].set_location(self.xy_next)
			#try to insert placing_piece at xy_next
				#if that's a legal placement
					#call self with the new placement (think about what to update)
					#if that solved it it'll get stopped at top, so it's false
					#so update what piece to try next
			print self.xy_next
			self.advance_next_placement()
		#out of possibilities
		return False	

#CONTENTS
#blueprint - list of coordinates on how to build the piece
#location - where placed on the board
#chat - what char used as an id/visual representation
class Piece:
	def __init__(self,blueprint_list = [], char_num = 65, *args):
		self.blueprint = blueprint_list
		self.location = False
		self.char = chr(char_num)

	def __repr__(self):
		return "Char: " + self.char + ", Blueprint: " + str(self.blueprint) + "\n"

	def set_location(self,xy_next = [], *args):
		self.location = xy_next