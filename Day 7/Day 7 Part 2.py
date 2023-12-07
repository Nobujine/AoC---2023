filename = 'Day 7/input.txt'

def determine_score(cards:str) -> int:
    card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    card_strength.reverse()  # to get increasing scores instead of starting at 0
    unique = ''.join(set(cards))
    count = max([cards.count(u) for u in unique.replace('J',' ')])

    # Part 2 Adjustment
    if 'J' in cards:
        count += 1 * cards.count('J')
        unique = unique.replace('J','')
    
    # Determine hand score
    match len(unique):
        case 1 | 0:
            score = 7 # Five of a kind or all Joker
        case 2:
            score = 6 if count == 4 else 5
        case 3:
            score = 4 if count == 3 else 3
        case 4:
            score = 2 # One pair
        case 5:
            score = 1  # High card
        case _:
            raise ValueError(f'We should not be here! {len(unique)=}')

    BASE_TEN_BUFFER = 10  # to ensure that when we concat to a string all numbers take up 2 digits minimum
    card_scores = [str(card_strength.index(c)+BASE_TEN_BUFFER) for c in cards]
    card_scores.insert(0, str(score+BASE_TEN_BUFFER))  # insert the hand score at the very front
    card_scores = int(''.join(card_scores))

    return card_scores

with open(filename, 'r') as f:
    all_hands = f.readlines()

all_hands = [hand.split() for hand in all_hands]
all_hands = [hand + [determine_score(hand[0])] for hand in all_hands]
all_hands.sort(key= lambda x: x[2])  # sort by the score at index 2

winnings = []
for i, hand in enumerate(all_hands):
    winnings.append(int(hand[1]) * (i+1))

print(f'Total Winnings: {sum(winnings)}')
...