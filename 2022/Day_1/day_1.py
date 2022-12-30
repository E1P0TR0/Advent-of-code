#!/usr/bin/env python3

"""
Advent-to-Code (day-1)
----------------------
statement: https://adventofcode.com/2022/day/1
"""

# | Day 1: Calorie Counting |

# Download input file in https://adventofcode.com/2022/day/1
with open('input.txt') as file:
	calories_group = [line.strip() for line in file.readlines()]

# part 1
calories_size = 0
_max = 0

for calories in calories_group:

	# if a group of calories ends, we look for the largest group
	if not calories:
		if calories_size >= _max:
			_max = calories_size
		calories_size = 0
	# else we continue to add calories to the current group
	else:
		calories_size += int(calories)

print('Part 1:', _max)

# part 2
calories_size = 0
calories_list = []

for calories in calories_group:
	# if a group of calories ends add to calories list
	if not calories:
		calories_list.append(calories_size)
		calories_size = 0
	# else we continue to add calories to the current group
	else:
		calories_size += int(calories)

# sort list to extract the top three most calories
calories_list.sort()
total = calories_list[-3:]
print('Part 2:', sum(total))