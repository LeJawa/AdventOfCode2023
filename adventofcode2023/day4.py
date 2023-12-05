input_file = "adventofcode2023/inputs/day4.txt"

def getWinningNumbers(line):
    return line.split(':')[1].split('|')[0].split()

def getPlayedNumbers(line):
    return line.split(':')[1].split('|')[1].split()

# Solution 1

sum = 0

with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        winningNumbers = getWinningNumbers(line)
        playedNumbers = getPlayedNumbers(line)
        
        winners = 0
        
        for number in playedNumbers:
            if number in winningNumbers:
                winners += 1
        
        if winners > 0:
            sum += 2**(winners-1)

print(sum)

# Solution 2

total_scratchcards = 0
scratchcard_winnings = [0]

with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        winningNumbers = getWinningNumbers(line)
        playedNumbers = getPlayedNumbers(line)
        
        winners = 0
        
        for number in playedNumbers:
            if number in winningNumbers:
                winners += 1
        
        if len(scratchcard_winnings) > 0:
            current_cards = 1 + scratchcard_winnings[0]
            scratchcard_winnings = scratchcard_winnings[1:]
        else:
            current_cards = 1
        
        total_scratchcards += current_cards
        
        for i in range(winners):
            if len(scratchcard_winnings) <= i:
                scratchcard_winnings.append(current_cards)
            else:
                scratchcard_winnings[i] += current_cards
        
print(total_scratchcards)