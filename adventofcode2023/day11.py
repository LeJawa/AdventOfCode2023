input_file = "adventofcode2023/inputs/day11.txt"

import numpy as np

tmp = []

with open(input_file, "r") as f:
    lines = f.readlines()
    
    for line in lines:
        if '#' in line:
            tmp.append(list(line.strip()))
        else:
            tmp.append(list(line.strip()))
            tmp.append(list(line.strip()))

tmp_t = np.array(tmp).T.tolist()
galaxy_t = []
for line in tmp_t:
    if '#' in line:
        galaxy_t.append(line)
    else:
        galaxy_t.append(line)
        galaxy_t.append(line)

galaxy = np.array(galaxy_t).T.tolist()

sum = 0
for y in range(len(galaxy)):
    for x in range(len(galaxy[y])):
        if galaxy[y][x] == '#':
            for i in range(y, len(galaxy)):
                for j in range(0, len(galaxy[i])):
                    if i == y and j <= x:
                        continue
                    
                    if galaxy[i][j] == '#':
                        distance = abs(i - y) + abs(j - x)
                        sum += distance

print(sum)
        