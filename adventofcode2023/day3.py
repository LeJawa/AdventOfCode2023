input_file = "adventofcode2023/inputs/day3_test.txt"

grid = []


with open(input_file, "r") as f:
    lines = f.readlines()
    
    for line in lines:
        grid.append(list(line))



## Solution 1

def is_machine_number(x, y):
    global grid
    def check(x, y):
        return not grid[y][x].isdigit() and grid[y][x] != '.' and grid[y][x] != '\n'
    
    if x > 0:
        if check(x - 1, y):
            return True
        if y > 0:
            if check(x - 1, y - 1):
                return True
        if y < len(grid) - 1:
            if check(x - 1, y + 1):
                return True
    if x < len(grid[0]) - 1:
        if check(x + 1, y):
            return True
        if y > 0:
            if check(x + 1, y - 1):
                return True
        if y < len(grid) - 1:
            if check(x + 1, y + 1):
                return True
    if y > 0:
        if check(x, y - 1):
            return True
    if y < len(grid) - 1:
        if check(x, y + 1):
            return True
    
    return False

number = ''
keep_number = False

sum = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        char = grid[y][x]
        if not char.isdigit():
            if keep_number:
                sum += int(number)
            number = ''
            keep_number = False
            continue
        
        number += char
        keep_number = keep_number or is_machine_number(x, y)

print(sum)

## Solution 2

def is_gear(x, y):
    global grid
    def check(x, y):
        return grid[y][x].isdigit()
    
    if grid[y][x] != '*':
        return False
    
    amountOfNumbers = 0