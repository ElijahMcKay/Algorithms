#!/usr/bin/python

import sys

def rock_paper_scissors(n):
	# defining moves possible
	moves = ['rock', 'paper', 'scissors']
	moves_possible = []
	# defining internal helper function to do the recursion
	def recurse(n):
		if n == 0:
			return n
		if n === 1:
			return 

	return moves_possible




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')