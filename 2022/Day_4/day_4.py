#!/usr/bin/env python3

"""
Advent-to-Code (day-4)
----------------------
statement: https://adventofcode.com/2022/day/4
"""

# Download file in https://adventofcode.com/2022/day/4
file_name = 'input.txt'
with open(file_name, 'r') as file:
    pairs = file.readlines()

# 4567 contains 345678
# ..345678.. 3-8
# ...4567... 4-7

# part 1
sum_contains = 0

for pair in pairs:
    # remove '\n'
    pair = pair.strip('\n')

    # divide in left side (3-8) and right side (4-7)
    left, right = pair.split(',')
    
    # function to divide by first (3) and last (8) each side
    first = lambda side: int(side.split('-')[0])
    last = lambda side: int(side.split('-')[1])

    # function to get the length of each side (8 - 3 = 5)
    length = lambda side: last(side) - first(side)
    
    # get max side (3-8) and min side (4-7) based on each range length (5 > 3)
    max_side, min_side = (left, right) if length(left) >= length(right) else (right, left)

    # validate if min side (4-7) contains max side (3-8) and add to total
    # ..345678..
    # ...4567...
    if first(min_side) >= first(max_side) and last(min_side) <= last(max_side):
        sum_contains += 1

print('Part 1:', sum_contains)

# part 2
sum_contains = 0
dont_overlap = 0

for pair in pairs:
    # remove '\n'
    pair = pair.strip('\n')

    # divide in left side (3-8) and right side (4-7)
    left, right = pair.split(',')
    
    # function to divide by first (3) and last (8) each side
    first = lambda side: int(side.split('-')[0])
    last = lambda side: int(side.split('-')[1])

    # get the min and max side based on the range closest to 0 ([3]-8 < [4]-7)
    min_side, max_side = (left, right) if first(left) <= first(right) else (right, left)

    # validate if min side (3-8) don't overlap max side (4-7)
    if last(min_side) < first(max_side):
        dont_overlap += 1

# calculate numbers of overlaps at all
sum_contains = len(pairs) - dont_overlap
print('Part 2:', sum_contains)