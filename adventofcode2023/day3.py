input_file = "adventofcode2023/inputs/day3.txt"

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

def is_gear_number(x, y):
    global grid
    def check(x, y):
        return grid[y][x] == '*'
    
    if x > 0:
        if check(x - 1, y):
            return True, x-1, y
        if y > 0:
            if check(x - 1, y - 1):
                return True, x-1, y-1
        if y < len(grid) - 1:
            if check(x - 1, y + 1):
                return True, x-1, y+1
    if x < len(grid[0]) - 1:
        if check(x + 1, y):
            return True, x+1, y
        if y > 0:
            if check(x + 1, y - 1):
                return True, x+1, y-1
        if y < len(grid) - 1:
            if check(x + 1, y + 1):
                return True, x+1, y+1
    if y > 0:
        if check(x, y - 1):
            return True, x, y-1
    if y < len(grid) - 1:
        if check(x, y + 1):
            return True, x, y+1
    
    return False, x, y

number = ''
gear_number = False
gears = {}
last_gear_x = -2
last_gear_y = -2


for y in range(len(grid)):
    for x in range(len(grid[0])):
        char = grid[y][x]
        if not char.isdigit():
            if gear_number:
                gears[(last_gear_x, last_gear_y)].append(int(number))
            number = ''
            gear_number = False
            continue
        
        number += char
        tmp_gear_number, gear_x, gear_y = is_gear_number(x, y)
        
        if tmp_gear_number:
            if (gear_x, gear_y) not in gears:
                gears[(gear_x, gear_y)] = []
            last_gear_x, last_gear_y = gear_x, gear_y
        
            gear_number = tmp_gear_number

sum = 0
for gear, numbers in gears.items():
    if len(numbers) == 2:
        sum += numbers[0] * numbers[1]

print(sum)