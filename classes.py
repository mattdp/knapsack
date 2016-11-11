#!/usr/bin/env python

class Board:
	#input: r_g_a array of zeros and hypens
	#
	#grid: array of array of strings. 0 = empty, - = not usable,
	#will be filled with piece ids over time
	#xy_next: [x,y] where placing first piece not in use
	#orient_next: int[0-3] with 0 up, 1 right, etc to orient piece
	#pieces: array of the pieces valid for this board
	#placing_piece: location in array of piece being placed at this call level
	def __init__(self,raw_grid_array = [], *args):
		self.grid = [list(line) for line in raw_grid_array]

class Piece:
	def __init__(self,raw_piece_array = [], *args):
		print "hi"