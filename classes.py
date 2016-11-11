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
		self.grid = [list(line) for line in grid_list]

		if len(piece_list) > 100:
			raise(AssertionError, "Weird stuff is going to happen with your chars")

		self.pieces = []
		char_num = 65 #ASCII 'A' - want lot of readable chars in a row
		for line in piece_list:
			self.pieces.append(Piece(line,char_num))
			char_num += 1

	def __repr__(self):
		return "Grid: " + str(self.grid) + "\nPieces: " + str(self.pieces)

class Piece:
	def __init__(self,coordinate_list = [], char_num = 65, *args):
		self.coordinates = coordinate_list
		self.char = chr(char_num)

	def __repr__(self):
		return "Char: " + self.char + ", Coordinates: " + str(self.coordinates) + "\n"