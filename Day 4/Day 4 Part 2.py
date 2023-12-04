import re

filename = 'Day 4/test_input.txt'

card_scores = []
with open(filename, 'r') as f:
    for card in f.read().splitlines():
        # Split of Card Number
        card_number, card = card.split(':')
        card_number = re.findall('Card[ ]+([0-9]+)', card_number)[0]

        # Parse winning numbers and my numbers
        winning_numbers, my_numbers = card.strip().split('|')
        winning_numbers = set(int(x) for x in winning_numbers.split(' ') if x != '')
        my_numbers =      set(int(x) for x in my_numbers.split(' ') if x != '')

        # intersection of the two sets
        winners = winning_numbers & my_numbers
        score = 2**(len(winners)-1) if winners else 0

        # Output Score
        print(f'Card {card_number}: {score}')
        card_scores.append(score)
        ...

print(f'Sum: {sum(card_scores)}')
...