input_file = "adventofcode2023/inputs/day7.txt"

hands = []
with open(input_file, "r") as f:
    lines = f.readlines()
    hands = [line.split() for line in lines]

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

def getabcde(hand):
    a, b, c, d, e = '', '', '', '', ''   
    
    if len(hand) == 0:
        return a, b, c, d, e
    
    a = hand[0]
    
    if len(hand) == 1:
        return a, b, c, d, e
    
    if hand[1] == hand[0]:
        a += hand[1]
    else:
        b = hand[1]
        
    if len(hand) == 2:
        return a, b, c, d, e
    
    if hand[2] == hand[0]:
        a += hand[2]
    elif hand[2] == hand[1]:
        b += hand[2]
    else:
        c = hand[2]
    
    if len(hand) == 3:
        return a, b, c, d, e
    
    if hand[3] == hand[0]:
        a += hand[3]
    elif hand[3] == hand[1]:
        b += hand[3]
    elif hand[3] == hand[2]:
        c += hand[3]
    else:
        d = hand[3]
    
    if len(hand) == 4:
        return a, b, c, d, e
        
    if hand[4] == hand[0]:
        a += hand[4]
    elif hand[4] == hand[1]:
        b += hand[4]
    elif hand[4] == hand[2]:
        c += hand[4]
    elif hand[4] == hand[3]:
        d += hand[4]
    else:
        e = hand[4]
    
    return a, b, c, d, e

for hand, bid in hands:    
    
    jokers = hand.count("J")
    modified_hand = hand.replace("J", "")
    
    a, b, c, d, e = getabcde(modified_hand) 
    
    # print(a, b, c, d, e)
    
    lengths = [len(a), len(b), len(c), len(d), len(e)]
    sorted_lengths = sorted(lengths, reverse=True)
    
    sorted_lengths[0] += jokers

    if sorted_lengths[0] >= 5:
        five_of_a_kind.append((hand, bid))
    elif sorted_lengths[0] == 4:
        four_of_a_kind.append((hand, bid))
    elif sorted_lengths[0] == 3:
        if sorted_lengths[1] == 2:
            full_house.append((hand, bid))
        else:
            three_of_a_kind.append((hand, bid))
    elif sorted_lengths[0] == 2:
        if sorted_lengths[1] == 2:
            two_pair.append((hand, bid))
        else:
            one_pair.append((hand, bid))
    else:
        high_card.append((hand, bid))
        
# print("five_of_a_kind", five_of_a_kind)
# print("four_of_a_kind", four_of_a_kind)
# print("full_house", full_house)
# print("three_of_a_kind", three_of_a_kind)
# print("two_pair", two_pair)
# print("one_pair", one_pair)
# print("high_card", high_card)

def card_value(card):
    card_values = "AKQT98765432J"
    return card_values.index(card)

import functools

def compare(hand1, hand2):
    if card_value(hand1[0][0]) == card_value(hand2[0][0]):
        if card_value(hand1[0][1]) == card_value(hand2[0][1]):
            if card_value(hand1[0][2]) == card_value(hand2[0][2]):
                if card_value(hand1[0][3]) == card_value(hand2[0][3]):
                    return card_value(hand1[0][4]) - card_value(hand2[0][4])
                return card_value(hand1[0][3]) - card_value(hand2[0][3])
            return card_value(hand1[0][2]) - card_value(hand2[0][2])
        return card_value(hand1[0][1]) - card_value(hand2[0][1])    
    return card_value(hand1[0][0]) - card_value(hand2[0][0])

def sort_hand_list(hand_list):
    return sorted(hand_list, key=functools.cmp_to_key(compare))

sorted_hands = sort_hand_list(five_of_a_kind)
sorted_hands.extend(sort_hand_list(four_of_a_kind))
sorted_hands.extend(sort_hand_list(full_house))
sorted_hands.extend(sort_hand_list(three_of_a_kind))
sorted_hands.extend(sort_hand_list(two_pair))
sorted_hands.extend(sort_hand_list(one_pair))
sorted_hands.extend(sort_hand_list(high_card))

# print(sorted_hands)

rank = len(sorted_hands)
winnings = 0

for _, bid in sorted_hands:
    winnings += rank * int(bid)
    rank -= 1

print(winnings)