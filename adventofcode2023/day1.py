input_file = "adventofcode2023/inputs/day1.txt"

## Solution 1
with open(input_file, "r") as f:
    lines = f.readlines()
    
    sum = 0
    for line in lines:
        digit1 = ""
        digit2 = ""
        
        for char in line:
            if char.isdigit():
                digit1 = char
                break
        for char in line[::-1]:
            if char.isdigit():
                digit2 = char
                break
            
        number = int(digit1 + digit2)
        sum += number

    print(sum)

## Solution 2
import re

pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

def parse(digit):
    if digit == "one":
        return "1"
    elif digit == "two":
        return "2"
    elif digit == "three":
        return "3"
    elif digit == "four":
        return "4"
    elif digit == "five":
        return "5"
    elif digit == "six":
        return "6"
    elif digit == "seven":
        return "7"
    elif digit == "eight":
        return "8"
    elif digit == "nine":
        return "9"
    else:
        return digit


with open(input_file, "r") as f:
    lines = f.readlines()
    
    sum = 0
    for line in lines:
        digits_found = [(m.start(0), m.end(1)) for m in re.finditer(pattern, line)]
        
        if len(digits_found) == 0:
            continue
        
        digit1 = line[digits_found[0][0]:digits_found[0][1]]
        digit2 = line[digits_found[-1][0]:digits_found[-1][1]]
        
        if len(digit1) > 1:
            digit1 = parse(digit1)
        
        if len(digit2) > 1:
            digit2 = parse(digit2)
        
        number = int(digit1 + digit2)
        sum += number

    print(sum)


