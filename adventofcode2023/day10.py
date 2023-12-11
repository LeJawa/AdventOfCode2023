input_file = "adventofcode2023/inputs/day10.txt"

class Pos:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: "Pos") -> "Pos":
        return Pos(self.x + other.x, self.y + other.y)
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Pos):
            return False
        return self.x == __value.x and self.y == __value.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    Up = lambda self: Pos(self.x, self.y - 1)
    Down = lambda self: Pos(self.x, self.y + 1)
    Left = lambda self: Pos(self.x - 1, self.y)
    Right = lambda self: Pos(self.x + 1, self.y)


starting_pos = Pos(-1, -1)

with open(input_file, "r") as f:
    lines = f.readlines()
    
    for line in lines:
        starting_pos.y += 1
        if "S" in line:
            starting_pos.x = line.index("S")
            break
    
    grid = [list(line.strip()) for line in lines]

def get(pos: Pos) -> str:
    return grid[pos.y][pos.x]

def get_first_connecting_pipes(pos: Pos) -> Pos:
    if get(pos.Up()) == "|" or get(pos.Up()) == "7" or get(pos.Up()) == "F":
        return pos.Up()
    elif get(pos.Down()) == "|" or get(pos.Down()) == "J" or get(pos.Down()) == "L":
        return pos.Down()
    elif get(pos.Left()) == "-" or get(pos.Left()) == "F" or get(pos.Left()) == "L":
        return pos.Left()
    else: # get(pos.Right()) == "-" or get(pos.Right()) == "7" or get(pos.Right()) == "J":
        return pos.Right()

def get_next_pos(current_pos: Pos, previous_pos: Pos) -> Pos:
    current_pipe = get(current_pos)
    
    if previous_pos == current_pos.Up():
        if current_pipe == "|":
            return current_pos.Down()
        elif current_pipe == "J":
            return current_pos.Left()
        else: # current_pipe == "L":
            return current_pos.Right()
    
    if previous_pos == current_pos.Down():
        if current_pipe == "|":
            return current_pos.Up()
        elif current_pipe == "7":
            return current_pos.Left()
        else: # current_pipe == "F":
            return current_pos.Right()
    
    if previous_pos == current_pos.Left():
        if current_pipe == "-":
            return current_pos.Right()
        elif current_pipe == "J":
            return current_pos.Up()
        else: # current_pipe == "7":
            return current_pos.Down()
    
    if previous_pos == current_pos.Right():
        if current_pipe == "-":
            return current_pos.Left()
        elif current_pipe == "L":
            return current_pos.Up()
        else: # current_pipe == "F":
            return current_pos.Down()
    
current_pos = get_first_connecting_pipes(starting_pos)
previous_pos = Pos(starting_pos.x, starting_pos.y)

steps = 1
while current_pos != starting_pos:
    next_pos = get_next_pos(current_pos, previous_pos)
    previous_pos = current_pos
    current_pos = next_pos
    steps += 1
    
print(steps//2)
