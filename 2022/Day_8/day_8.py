#!/usr/bin/env python3

"""
Advent-to-Code (day-8)
----------------------
statement: https://adventofcode.com/2022/day/8
"""

# Download file in https://adventofcode.com/2022/day/8
with open('input.txt') as file:
	trees = [line.strip() for line in file]

# part 1
visible_trees = 0
for position, group_tree in enumerate(trees):
	# ignore first and last row
	if position == 0 or position == len(trees) - 1:
		continue

	for column in range(len(group_tree)):
		# ignore first and last column
		if column == 0 or column == len(group_tree) - 1:
			continue
		
		# get maximun of each horizontal side
		horizontal_tallest_tree_left = max(group_tree[0:column])
		horizontal_tallest_tree_right = max(group_tree[column + 1:])
		
		# get maximun of each vertical side
		vertical_tallest_tree_up = max([trees[row][column] for row in range(0, position)])
		vertical_tallest_tree_down = max([trees[row][column] for row in range(position + 1, len(trees))])
		
		# if the current tree has no view from all our sides
		if (group_tree[column] <= horizontal_tallest_tree_left and
		  	group_tree[column] <= horizontal_tallest_tree_right and
			group_tree[column] <= vertical_tallest_tree_up and
			group_tree[column] <= vertical_tallest_tree_down):
			continue

		visible_trees += 1

# add all border trees
default_visible = ( (len(group_tree) + len(trees)) * 2) - 4

print('Part 1:', default_visible + visible_trees)


# part 2
highest_scenic = 0

# function to calculate trees visible from the current tree horizontal view
def trees_count_hor(_range):
	count = 0
	for tree in _range:
		if tree >= group_tree[column]:
			count += 1
			break

		count += 1

	return count

# function to calculate trees visible from the current tree vertical view
def trees_count_ver(_range):
	count = 0
	for row in _range:
		if trees[row][column] >= group_tree[column]:
			count += 1
			break

		count += 1

	return count

for position, group_tree in enumerate(trees):
	# ignore first and last row
	if position == 0 or position == len(trees) - 1:
		continue
	
	scenic_score = 0
	for column in range(len(group_tree)):
		# ignore first and last columns
		if column == 0 or column == len(group_tree) - 1:
			continue

		# calculate visible trees of each side
		visible_tree_count_left = trees_count_hor(reversed(group_tree[0:column]))
		visible_tree_count_right = trees_count_hor(group_tree[column + 1:])

		visible_tree_count_up = trees_count_ver(reversed(range(0, position)))
		visible_tree_count_down = trees_count_ver(range(position + 1, len(trees)))

		# calculate the highest scenic score
		scenic_score = visible_tree_count_left \
						* visible_tree_count_right \
						* visible_tree_count_up \
						* visible_tree_count_down

		if scenic_score >= highest_scenic:
			highest_scenic = scenic_score


print('Part 2:', highest_scenic)