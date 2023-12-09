input_file = "adventofcode2023/inputs/day9.txt"

histories = []
with open(input_file, "r") as f:
    lines = f.readlines()
    histories = list(map(lambda line: [int(x) for x in line.split()], lines))

def get_diff_sequence(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

def all_zeroes(sequence):
    return all([x == 0 for x in sequence])

next_predictions = []
before_predictions = []

for history in histories:
    last_values_in_sequence = []
    first_values_in_sequence = []
    sequence = history.copy()
    
    while not all_zeroes(sequence):
        last_values_in_sequence.append(sequence[-1])
        first_values_in_sequence.append(sequence[0])
        sequence = get_diff_sequence(sequence)
    
    next_predictions.append(sum(last_values_in_sequence))
    
    before_prediction = 0
    for value in first_values_in_sequence[::-1]:
        before_prediction = value - before_prediction
    
    before_predictions.append(before_prediction)

# Solution 1
print(sum(next_predictions))

# Solution 2
print(sum(before_predictions))


        
        
