#!/usr/bin/env python

from copy import deepcopy
from IPython import embed

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
class Board(object):
	def __init__(self,grid_list = [], piece_list = [], xy_next = [0,0], placing_piece = 0, *args):
		self.xy_next = xy_next
		self.placing_piece = placing_piece
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

	def in_bounds_test(self,location = [], *args):
		vb = self.valid_bounds()
		return (location[0] < vb[0] and location[1] < vb[1])

	# can error if coordinates invalid
	def empty_grid_test(self,location = [], *args):
		return ("0" == self.grid[location[0]][location[1]])


# IN OLD BOARD
# In [1]: type(self.pieces[self.placing_piece].blueprint)
# Out[1]: list

# INSIDE THE NEW CREATED BOARD
# In [9]: type(self.pieces[0].blueprint)
# Out[9]: <probably a piece now>

	#not DRY (place_piece), refactor when add orientation
	def valid_placement_test(self):
		abs_location = [0,0]
		for rel_location in self.pieces[self.placing_piece].blueprint:
			for i in [0,1]:
				abs_location[i] = rel_location[i] + self.xy_next[i]
			if (self.in_bounds_test(abs_location) and self.empty_grid_test(abs_location)):
				next
			else: 
				return False 
		return True

	#not smart. will overflow bounds
	def advance_next_placement(self):
		x = self.xy_next[0]
		if x < (self.valid_bounds()[0] - 1):
			self.xy_next[0] += 1
		else:
			self.xy_next[0] = 0
			self.xy_next[1] += 1

	#not DRY (valid_placement_test), refactor when add orientation
	def place_piece(self, piece = None, xy_next = [0,0]):
		abs_location = [0,0]
		for rel_location in piece.blueprint:
			for i in [0,1]:
				abs_location[i] = rel_location[i] + self.xy_next[i]
			self.grid[abs_location[0]][abs_location[1]] = piece.char
		return True

	#returns either a board or False. Recursive.
	def attempt_solve(self):
		if (self.placing_piece >= len(self.pieces)):
			return self

		piece = self.pieces[self.placing_piece]

		while (self.in_bounds_test(self.xy_next)):
			if self.valid_placement_test():

				#RIGHT NOW PIECES CAN GO ON TOP OF EACH OTHER
				#NEED TO UPDATE GRID IN PLACE_PIECE
				
				#note that pieces not copied, since not changed
				b = Board(deepcopy(self.grid), self.pieces, [0,0], self.placing_piece + 1 )
				b.place_piece(piece,self.xy_next)
				print b
				b.attempt_solve() #will be caught at top of next call at this level if a win

			self.advance_next_placement()
		#out of possibilities
		return False	

#CONTENTS
#blueprint - list of coordinates on how to build the piece
#location - where placed on the board
#chat - what char used as an id/visual representation
class Piece(object):
	def __init__(self,blueprint_list = [], char_num = 65, *args):
		self.blueprint = blueprint_list
		self.char = chr(char_num)

	def __repr__(self):
		return "Char: " + self.char + ", Blueprint: " + str(self.blueprint) + "\n"