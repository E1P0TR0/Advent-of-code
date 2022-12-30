#!/usr/bin/env python3

"""
Advent-to-Code (day-3)
----------------------
statement: https://adventofcode.com/2022/day/3
"""

from re import findall
from string import ascii_lowercase

# Download file in https://adventofcode.com/2022/day/3
file_name = 'input.txt'

# priority values
# a -> z (1, 26)
# A -> Z (27, 52)

# part1
sum_priorities = 0
rucksacks = open(file_name, 'r')

for items in rucksacks:
    # divide items
    left_half, right_half = items[:len(items)//2], items[len(items)//2:]

    # remove duplicates
    left_half = ''.join(set(left_half))
    right_half = ''.join(set(right_half))

    # extract equals items in each half
    left_half_pattern = r'[{}]'.format(left_half)
    duplicate_item = findall(left_half_pattern, right_half)[0]

    # calculate item priority and add to total
    if duplicate_item in ascii_lowercase:
        diff = 96
    else:
        diff = 38

    sum_priorities += (ord(duplicate_item) - diff)

rucksacks.close()
print('part1', sum_priorities)


# part2
sum_priorities = 0
rucksacks = open(file_name, 'r')
rucksacks = list(rucksacks)

for pos in range(0, len(rucksacks), 3):
    # group of 3
    first  = rucksacks[pos].strip()
    second = rucksacks[pos + 1].strip()
    third  = rucksacks[pos + 2].strip()

    # remove duplicates
    first, second, third = ''.join(set(first)), ''.join(set(second)), ''.join(set(third))

    # extract duplicates by group (like part 1)
    first_pattern = r'[{}]'.format(first)
    duplicate_items = findall(first_pattern, second)

    duplicate_items = ''.join([str(i) for i in duplicate_items]) # (list to string)
    second_patter = r'[{}]'.format(duplicate_items)
    duplicate_items = findall(second_patter, third)[0]

    # calculate item priority and add to total
    if duplicate_items in ascii_lowercase:
        diff = 96
    else:
        diff = 38

    sum_priorities += (ord(duplicate_items) - diff)

print('part2:', sum_priorities)