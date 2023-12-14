input_file = "adventofcode2023/inputs/day14.txt"

with open(input_file, "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    
    
# for line in lines:
#     print("".join(line))

# print("")

for y in range(len(lines)):    
    for x in range(len(lines[y])):
        if lines[y][x] != 'O':
            continue
        
        movement = 0
        while y - movement >= 0:
            movement += 1
            
            if lines[y - movement][x] != '.':
                break
        
        movement -= 1
        
        lines[y][x] = '.'
        lines[y - movement][x] = 'O'

# for line in lines:
#     print("".join(line))

load = 0
for i in range(len(lines)):
    load += lines[i].count('O') * (len(lines) - i)

print(load)
        
            
    
