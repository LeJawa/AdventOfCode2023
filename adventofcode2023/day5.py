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
        for dest, source, rng in map:
            if seed >= source and seed < source + rng:
                seed = dest + (seed - source)
                break
    locations.append(seed)

print(min(locations))

# Solution 2
seed_ranges = []

for i in range(len(seeds) // 2):
    seed_ranges.append((seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1] - 1))

locations = []

seed_start = seed_ranges[0][0]
seed_end = seed_start + seed_ranges[0][1] - 1
ranges = seed_ranges

for map in maps:
    next_map_ranges = []
    for dest, source, rng in map:
        next_ranges = []
        for seed_start, seed_end in ranges:
            range_before = (
                (seed_start, min(source - 1, seed_end))
                if seed_start < source
                else None
            )
            range_after = (
                (max(source + rng, seed_start), seed_end)
                if seed_end > source + rng
                else None
            )

            range_between = (
                (
                    max(source, seed_start) - source + dest,
                    min(source + rng - 1, seed_end) - source + dest,
                )
                if (seed_start >= source and seed_start < source + rng)
                or (seed_end < source + rng and seed_end >= source)
                else None
            )

            if range_between:
                next_map_ranges.append(range_between)
            
                if range_before:
                    next_ranges.append(range_before)
                if range_after:
                    next_ranges.append(range_after)
            else:
                next_ranges.append((seed_start, seed_end))
        ranges = next_ranges
    ranges += next_map_ranges

print(min([x[0] for x in next_ranges]))

