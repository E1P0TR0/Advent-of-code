#!/usr/bin/env python3

"""
Advent-to-Code (day-7)
----------------------
statement: https://adventofcode.com/2022/day/7
"""

# Total size directories: a(e(584) + f(29116)) + e(584)

# Download file in https://adventofcode.com/2022/day/7
with open('input.txt', 'r') as file:
    commands = [line.strip() for line in file.readlines()]

# part 1
current_dir = []
current_dir_size = {}
MAX_SIZE = 100000

current_dir_path = lambda: '/'.join(current_dir)
valid_size = lambda value: True if value <= MAX_SIZE else False

total_size = 0
for line in commands:
    # move to specific directory
    if line[0] == '$':
        command = line.split(' ')
        if command[1] == 'ls':
            pass
        elif command[1] == 'cd':
            # init root direcory
            if command[2] == '/':
                current_dir_size = {'/':0}
            # go back one directory
            elif command[2] == '..':
                current_dir.pop()
            # go to directory
            else:
                current_dir.append(command[2])
    elif line[0:3] == 'dir':
        pass
    # sum files of current directory
    else:
        file_size = line.split(' ')[0]
        dir_path = current_dir_path()

        # calculate size of '/' directory
        current_dir_size['/'] += int(file_size)
        while '/' in dir_path:
            if dir_path == '/': 
                break
            # init directory
            if current_dir_size.get(dir_path) == None:
                current_dir_size[dir_path] = 0

            # add sum files of current directory
            current_dir_size[dir_path] += int(file_size)

            # go to parent directory
            dir_split = dir_path.split('/')
            dir_split.pop()
            dir_path = '/'.join(dir_split)

# add the size of all directories
for key in current_dir_size:
    size = current_dir_size[key]
    if valid_size(size):
        total_size += size

print('Part 1:', total_size)

# part2
# total disk space available and unused to the filesystem
AVAILABLE = 70000000
MIN_UNUSED = 30000000

space_to_remove = MIN_UNUSED - (AVAILABLE - current_dir_size['/'])

valid_sizes = []
for key in current_dir_size:
    size = current_dir_size[key]
    # calculate all sizes to minimum unused space required
    if size >= space_to_remove:
        valid_sizes.append(size)

print('Part 2:', min(valid_sizes))