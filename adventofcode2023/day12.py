input_file = "adventofcode2023/inputs/day12.txt"

rows = []
damaged_springs = []

with open(input_file, "r") as f:
    lines = f.readlines()
    
    rows = [line.split()[0] for line in lines]
    damaged_springs = [[int(x) for x in line.split()[1].split(',')] for line in lines]

# print(rows)
# print(damaged_springs)

def create_regex_pattern(damaged_spring):
    pattern = r'^\.*'
    
    for n in damaged_spring:
        pattern += f'#{{{n}}}\.+'
        
    pattern = '*'.join(pattern.rsplit('+', 1)) + '$'
    return pattern

import re

def is_valid_row(row, pattern):
    return re.match(pattern, row) is not None

def binary_representation(n, length):
    return bin(n)[2:].zfill(length)

good_arrangements = 0

for row_index in range(len(rows)):
    missing = rows[row_index].count('?')    
    pattern = create_regex_pattern(damaged_springs[row_index])

    
    for arrangement in range(2**missing):
        completed_row = rows[row_index]
        for i in binary_representation(arrangement, missing):
            if i == '0':
                option = '.'
            else:
                option = '#'
            completed_row = completed_row.replace('?', option, 1)
        if is_valid_row(completed_row, pattern):
            good_arrangements += 1

print(good_arrangements)
            
            
            
    
    
    
    
