input_file = "adventofcode2023/inputs/day13_test.txt"

patterns = []

with open(input_file, "r") as f:
    lines = f.readlines()
    
    pattern = []
    for line in lines:        
        if line == '\n':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append([0 if c == '.' else 1 for c in line.strip()])
    patterns.append(pattern)

# print(patterns)

import numpy as np

for pattern in patterns:
    array = np.array(pattern)
    
    # array[0]
    for i in range(array.shape[0]-1):
        if (array[i+1] == array[i]).all():
            reflection = True
            j, k = i-1, i+1
            while j >= 0 and k < array.shape[0]:
                if (array[j] == array[k]).all():
                    j -= 1
                    k += 1
                else:
                    reflection = False
                    break
            if reflection:
                print(i, i+1)
            
            print("----------------")
    
    
    # array[:,0]
    
    
