import re

red_cubes= 12
green_cubes= 13
blue_cubes= 14

input_file = "adventofcode2023/inputs/day2.txt"

sum = 0
with open(input_file, "r") as f:
    lines = f.readlines()
    for game in lines:
        game_number = int(game.split(":")[0].split(" ")[1])
        game_records = game.split(":")[1].split(";")
        
        good_game = True
        for record in game_records:
            red = re.findall(r"(\d+) red", record)
            green = re.findall(r"(\d+) green", record)
            blue = re.findall(r"(\d+) blue", record)
            
            if len(red) > 1 or len(green) > 1 or len(blue) > 1:
                print("Game: " + game_number)
                print("Red: " + str(red))
                print("Green: " + str(green))
                print("Blue: " + str(blue))
                print("Record: " + record)
            
            red = int(red[0]) if len(red) > 0 else 0
            green = int(green[0]) if len(green) > 0 else 0
            blue = int(blue[0]) if len(blue) > 0 else 0
            
            if red > red_cubes or green > green_cubes or blue > blue_cubes:
                good_game = False
                break
        
        if good_game:
            sum += game_number
        
print ("Sum of possible games: " + str(sum))

sum = 0
with open(input_file, 'r') as f:
    lines = f.readlines()
    
    for game in lines:
        game_records = game.split(":")[1].split(";")
        
        min_red = 1
        min_green = 1
        min_blue = 1
    
        for record in game_records:
            red = re.findall(r"(\d+) red", record)
            green = re.findall(r"(\d+) green", record)
            blue = re.findall(r"(\d+) blue", record)
            
            if len(red) > 1 or len(green) > 1 or len(blue) > 1:
                print("Game: " + game_number)
                print("Red: " + str(red))
                print("Green: " + str(green))
                print("Blue: " + str(blue))
                print("Record: " + record)
            
            red = int(red[0]) if len(red) > 0 else 0
            green = int(green[0]) if len(green) > 0 else 0
            blue = int(blue[0]) if len(blue) > 0 else 0
            
            if red > min_red:
                min_red = red
            if green > min_green:
                min_green = green
            if blue > min_blue:
                min_blue = blue
        
        power = min_red * min_green * min_blue
        sum += power
print("Sum of power: " + str(sum))
        
    
    