input_file = "adventofcode2023/inputs/day11.txt"

import numpy as np

tmp = []

galaxies_list = []

expansion_indices_y = []
expansion_indices_x = []

with open(input_file, "r") as f:
    lines = f.readlines()
    
    for y in range(len(lines)):
        galaxy_found = False
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                galaxies_list.append((x, y))
                galaxy_found = True
                
        if galaxy_found:
            tmp.append(list(lines[y].strip()))
        else:
            tmp.append(['+'] * len(lines[y].strip()))
            expansion_indices_y.append(y)

tmp_t = np.array(tmp).T.tolist()
galaxy_t = []

for x in range(len(tmp_t)):
    galaxy_found = False
    for y in range(len(tmp_t[x])):
        if tmp_t[x][y] == '#':
            galaxy_found = True
            
    if galaxy_found:
        galaxy_t.append(tmp_t[x])
    else:
        galaxy_t.append(['+'] * len(tmp_t[x]))
        expansion_indices_x.append(x)

galaxy = np.array(galaxy_t).T.tolist()

# print(expansion_indices_x)
# print(expansion_indices_y)

# for line in galaxy:
#     print("".join(line))

def calculate_sum_of_distances(expansion):
    sum = 0
    for y in range(len(galaxy)):
        for x in range(len(galaxy[y])):
            if galaxy[y][x] == '#':
                for i in range(y, len(galaxy)):
                    for j in range(0, len(galaxy[i])):
                        if i == y and j <= x:
                            continue
                        
                        if galaxy[i][j] == '#':
                            # print("({}, {}) -> ({}, {})".format(x, y, j, i))
                            
                            spaces = 0
                            for index in expansion_indices_y:
                                if index > y and index < i or index < y and index > i:
                                    spaces += expansion - 1
                            for index in expansion_indices_x:
                                if index > x and index < j or index < x and index > j:
                                    spaces += expansion - 1
                            
                            distance = abs(i - y) + abs(j - x)
                            
                            # print("Spaces: {}".format(spaces))
                            # print("Distance: {}".format(distance))
                            sum += distance + spaces
    return sum

# Solution 1
sum = calculate_sum_of_distances(2)
print(sum)

# Solution 2
sum = int(calculate_sum_of_distances(1e6))
print(sum)
        