input_file = "adventofcode2023/inputs/day5.txt"

maps = []
seeds = []

with open(input_file) as f:
    lines = f.readlines()
    
    current_map = []
    mapping = False
    for line in lines:
        if "seeds" in line:
            seeds = [int(x) for x in line.split(":")[1].split()]
            continue
        
        if "map" in line:
            if mapping:
                maps.append(current_map)
                current_map = []
            else:
                mapping = True
            continue
        
        numbers = line.split()
        
        if len(numbers) == 3:
            current_map.append([int(x) for x in numbers]) 
    
    maps.append(current_map)

# Solution 1

locations = []
for seed in seeds:
    for map in maps:
        for (dest, source, rng) in map:
            if seed >= source and seed < source + rng:
                seed = dest + (seed - source)
                break
    locations.append(seed)

print(min(locations))

# Solution 2
new_seeds = []

for i in range(len(seeds) // 2):
    for j in range(seeds[i*2 + 1]):
        new_seeds.append(seeds[i*2] + j)

print(len(new_seeds))

locations = []
i = 0
for seed in new_seeds:
    if i / len(new_seeds) * 100 % 1 == 0:
        print(f"{i / len(new_seeds) * 100}%")
    for map in maps:
        for (dest, source, rng) in map:
            if seed >= source and seed < source + rng:
                seed = dest + (seed - source)
                break
    locations.append(seed)
    i += 1

print(min(locations))
    