input_file = "adventofcode2023/inputs/day6.txt"

# Solution 1

times = []
distances = []

with open(input_file, "r") as f:
    lines = f.readlines()
    
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]

numberOfRaces = len(times)

factor = 1

for i in range(numberOfRaces):
    waysToWin = 0
    for t in range(times[i]):
        remainingTime = times[i] - t
        
        if t * remainingTime > distances[i]:
            waysToWin += 1
    factor *= waysToWin

print(factor)

# Solution 2

with open(input_file, "r") as f:
    lines = f.readlines()
    
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

waysToWin = 0
startOfWinning = 0
endOfWinning = time

for t in range(time):
    remainingTime = time - t
    
    if t * remainingTime > distance:
        startOfWinning = t
        
for t in range(time, 0, -1):
    remainingTime = time - t
    
    if t * remainingTime > distance:
        endOfWinning = t

waysToWin = startOfWinning - endOfWinning + 1

print(waysToWin)