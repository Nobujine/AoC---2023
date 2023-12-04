filename = 'Day 4/input.txt'

card_scores = {}
card_copies = {}
with open(filename, 'r') as f:
    for card in f.read().splitlines():
        # Split of Card Number
        card_number, card = card.split(':')
        card_number = int(card_number.split(' ')[-1])

        # Parse winning numbers and my numbers
        winning_numbers, my_numbers = card.strip().split('|')
        winning_numbers = set(int(x) for x in winning_numbers.split(' ') if x != '')
        my_numbers =      set(int(x) for x in my_numbers.split(' ') if x != '')

        # intersection of the two sets
        winners = winning_numbers & my_numbers
        card_scores[card_number] = len(winners)
        card_copies[card_number] = 1  # Set initial number of cards to 1

# Generate number of copies of cards
for card_number, score in card_scores.items():
    for i in range(card_copies[card_number]):
        for i in range(score):
            target_card = card_number+i+1
            if target_card in card_copies:
                card_copies[target_card] += 1 

print(f'Sum: {sum(card_copies.values())}')
...