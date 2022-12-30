#!/usr/bin/env python3

"""
Advent-to-Code (day-2)
----------------------
statement: https://adventofcode.com/2022/day/2
"""

# | Day 2: Rock Paper Scissors |

# Download input file in https://adventofcode.com/2022/day/2
with open('input.txt') as file:
	tournament = [line.strip() for line in file.readlines()]

# part 1
play = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
_round = {'lose':0, 'draw':3, 'won':6}

total_score = 0

# A X = 0  (d)
# A Y = -1 (w)
# A Z = -2 (l)
# B X = 1  (l)
# B Y = 0  (d)
# B Z = -1 (w)
# C X = 2  (w)
# C Y = 1  (l)
# C Z = 0  (d)

for game in tournament:

	opp, me = game.split(' ')
	result = play[opp] - play[me]
	
	if result == 0:
		total_score += (play[me] + _round['draw'])
	elif result == -1 or result == 2:
		total_score += (play[me] + _round['won'])
	else:
		total_score += (play[me] + _round['lose'])

print('Part 1:', total_score)

# part 2
total_score = 0

# X -> lose
# Y -> draw
# Z -> won

for game in tournament:

	opp, result = game.split(' ')
	
	if result == 'X':
		total_score += _round['lose']

		if opp == 'A':
			total_score += play['Z']
		elif opp == 'B':
			total_score += play['X']
		else:
			total_score += play['Y']
	
	elif result == 'Z':
		total_score += _round['won']

		if opp == 'A':
			total_score += play['Y']
		elif opp == 'B':
			total_score += play['Z']
		else:
			total_score += play['X']
	else:
		total_score += (play[opp] + _round['draw'])

print('Part 2:', total_score)