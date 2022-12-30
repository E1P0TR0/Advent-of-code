#!/usr/bin/env python3

"""
Advent-to-Code (day-5)
----------------------
statement: https://adventofcode.com/2022/day/5
"""

from copy import deepcopy

# Download file in https://adventofcode.com/2022/day/5
file_name = 'input.txt'
with open(file_name, 'r') as file:
    moves = file.readlines()

#     [D]            [D]        
# [N] [C]      ->    [N] [C]  
# [Z] [M] [P]        [Z] [M] [P]
#  1   2   3          1   2   3
#
# move 1 from 2 to 1

# Create your matrix manually
stack_crates = [
    ['W', 'M', 'L', 'F'],
    ['B', 'Z', 'V', 'M', 'F'],
    ['H', 'V', 'R', 'S', 'L', 'Q'],
    ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
    ['L', 'S', 'W'],
    ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
    ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
    ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
    ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W'],
]

# part 1
stack_crates_cp_1 = deepcopy(stack_crates[:]) # list copy

for move in moves:
    # separate data per ' '
    move = move.split(' ')
    # save specific value of each action
    _move, _from, _to = int(move[1]), int(move[3]), int(move[5])
    # move "n" times (_move) last value of specific list (_from) and add to another (_to)
    while _move > 0:
        item_removed = stack_crates_cp_1[_from - 1].pop()
        stack_crates_cp_1[_to - 1].append(item_removed)
        _move -= 1

all_tops = ''
for crates in stack_crates_cp_1:
    all_tops += crates[-1]

print('Part 1:', all_tops)

# part 2
stack_crates_cp_2 = deepcopy(stack_crates[:])

for move in moves:
    # separate data per ' '
    move = move.split(' ')
    # save specific value of each action
    _move, _from, _to = int(move[1]), int(move[3]), int(move[5])
    # move "n" times (_move) last value of specific list (_from) to a temporary list
    tmp_list = []
    while _move > 0:
        item_removed = stack_crates_cp_2[_from - 1].pop()
        tmp_list.append(item_removed)
        _move -= 1
    # add inverted temporary list to another list (_to)
    stack_crates_cp_2[_to - 1].extend(tmp_list[::-1])

all_tops = ''
for crates in stack_crates_cp_2:
    all_tops += crates[-1]

print('Part 2 (v1):', all_tops)

# part 2 (alternative)
stack_crates_cp_3 = stack_crates[:]

for move in moves:
    # separate data per ' '
    move = move.split(' ')
    # save specific value of each action
    _move, _from, _to = int(move[1]), int(move[3]), int(move[5])
    # split the list in two:
    # (1) The sublist to move
    tmp_list = stack_crates_cp_3[_from - 1][(len(stack_crates_cp_3[_from - 1]) - _move):]
    # (2) The sublist that is kept 
    stack_crates_cp_3[_from - 1] = stack_crates_cp_3[_from - 1][:(len(stack_crates_cp_3[_from - 1]) - _move)]
    # add temporary list to another list (_to)
    stack_crates_cp_3[_to - 1].extend(tmp_list)

all_tops = ''
for crates in stack_crates_cp_3:
    all_tops += crates[-1]

print('Part 2 (v2):', all_tops)