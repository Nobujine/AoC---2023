filename = 'Day 7/input.txt'

def determine_score(cards:str) -> int:
    card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']
    card_strength.reverse()  # to get increasing scores instead of starting at 0
    unique = ''.join(set(cards))
    count = max([cards.count(u) for u in unique.replace('J',' ')])
    # ['Q2KJJ', '13', 2111221010]
    # Part 2 Adjustment
    if 'J' in cards:
        count += 1 * cards.count('J')
        unique = unique.replace('J','')

    score = 0
    HAND_MULTIPLIER = 1_000_000_000_000
    match len(unique):
        case 1 | 0:
            score = 7 * HAND_MULTIPLIER # Five of a kind or all Joker
        case 2:
            if count == 4:
                score = 6 * HAND_MULTIPLIER  # Four of a kind
            elif count == 3:
                score = 5 * HAND_MULTIPLIER # Full House
        case 3:
            if count == 3:
                score = 4 * HAND_MULTIPLIER  # Three of a kind
            elif count == 2:
                score = 3 * HAND_MULTIPLIER # Two pair
        case 4:
            if count == 2:
                score = 2 * HAND_MULTIPLIER # One pair
        case 5:
            score = 1 * HAND_MULTIPLIER  # High card
        case _:
            raise ValueError(f'We should not be here! {len(unique)=}')
    BASE_TEN_BUFFER = 10  # to ensure that when we concat to a string all numbers take up 2 digits minimum
    card_scores = [str(card_strength.index(c)+BASE_TEN_BUFFER) for c in cards]
    card_scores = int(''.join(card_scores))
    score += card_scores
    return score

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