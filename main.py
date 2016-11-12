#!/usr/bin/env python

from classes import Board
from copy import deepcopy

def scenario_parser(filename):
	file = open(filename)
	lines = [line.replace("\n","") for line in file.readlines()]
	grid_input = []
	pieces = []

	i = 0
	while (i < len(lines) and lines[i]): #will be false if empty string, new to me
		grid_input.append(lines[i])
		i += 1
	
	i += 1 #skip the blank string it ended on

	number_of_pieces = int(lines[i])
	i += 1

	one_piece = []
	while (i < len(lines)):
		if lines[i]:
			one_piece.append(lines[i])
		else:
			pieces.append(deepcopy(one_piece))
			one_piece = []
		i += 1

	if one_piece:
		pieces.append(deepcopy(one_piece))

	if len(pieces) != number_of_pieces:
		print lines
		print one_piece, len(pieces), number_of_pieces
		raise(AssertionError, "Mismatched number of pieces")

	return Board(grid_input,pieces)

board = scenario_parser("base.scenario")
print board.attempt_solve()