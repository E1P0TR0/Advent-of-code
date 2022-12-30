#!/usr/bin/env python3

"""
Advent-to-Code (day-6)
----------------------
statement: https://adventofcode.com/2022/day/6
"""

# Problem:
# 1st four sequence different
# fnggalrneldjsjods
#    |__|

# Download file in https://adventofcode.com/2022/day/6
file_name = 'input.txt'
stream = open(file_name, 'r').read()

# general functiom
def start_of_message(stream_len):
        for byte in range(0, len(stream)):
                # group stream stream_len by stream_len
                group_stream = stream[byte:byte+stream_len]
                # create temp list
                tmp_list = []
                # filter unique bytes from stream
                filter_stream = [tmp_list.append(b) for b in group_stream if b not in tmp_list]
                # check if a byte of stream is repeated
                if len(filter_stream) < stream_len:
                        continue
                else:
                        del tmp_list
                        return byte+stream_len

# maim flow
if __name__ == '__main__':
        print('[*] Part 1:', start_of_message(4))
        print('[*] Part 2:', start_of_message(14))