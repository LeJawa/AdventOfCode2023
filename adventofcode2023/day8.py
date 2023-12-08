input_file = "adventofcode2023/inputs/day8.txt"

import re

instructions = []

nodes = {}

with open(input_file, "r") as f:
    lines = f.readlines()
    
    instructions = list(lines[0].strip())
    
    nodePattern = r"(\w{3}) = \((\w{3}), (\w{3})\)"
    
    for line in lines[2:]:
        
        match = re.finditer(nodePattern, (line), re.MULTILINE).__next__()
        
        nodes[match.group(1)] = {
            "L": match.group(2),
            "R": match.group(3)
        }

index = 0
def next_instruction():
    global instructions, index
    
    if index >= len(instructions):
        index = 0

    instruction = instructions[index]
    index += 1
    
    return instruction

def next_node(node, instruction = None):
    global nodes
    
    return nodes[node][instruction or next_instruction()]

# Solution 1

steps = 0
try:
    current_node = "AAA"

    while current_node != "ZZZ":
        current_node = next_node(current_node)
        steps += 1

    print(steps)
except Exception as e:
    pass

# Solution 2

start_nodes = []

for node in nodes.keys():
    if node[2] == 'A':
        start_nodes.append(node)

def node_is_end(node):
    return node[2] == 'Z'

def all_nodes_are_end(nodes):
    for node in nodes:
        if not node_is_end(node):
            return False
    return True

steps = 0

number_of_nodes = len(start_nodes)

last_steps = 0
intervals = [0 for _ in range(number_of_nodes)]

for i in range(number_of_nodes):
    index = 0
    for _ in range(50000):
        start_nodes[i] = next_node(start_nodes[i])        
        steps += 1
        
        if node_is_end(start_nodes[i]):
            interval = steps - last_steps
            last_steps = steps
            intervals[i] = interval  


from math import gcd

lcm = 1
for i in intervals:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

    
