import re
import math

filename = 'Day 3/input.txt'

def distance(a:tuple, b:tuple):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def check_number(positions:tuple, symbols:tuple) -> bool:
    for position in positions:
        for symbol in symbols:
            if distance(position, symbol) == 1:
                return True
    return False

# Get all symbols
symbols = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.readlines()):
        for symbol in re.finditer(r'([*])', line):
            x = symbol.span()[0]
            symbols.append((x,y,symbol.group()[0]))

# Parse for numbers, check adjacent cells        
numbers = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.readlines()):
        for number in re.finditer('([0-9]+)', line):
            x = number.span()[0]
            number_text = number.group()
            positions = [(x+i,y) for i in range(len(number_text))]
            if check_number(positions, symbols):
                numbers.append(((x,y),number_text))

# match numbers based on proximity to *
gear_ratios = []
for symbol in symbols:
    gear_numbers = []
    for number in numbers:
        positions = [(number[0][0]+i,number[0][1]) for i in range(len(number[1]))]
        if check_number(positions, [symbol]) == 1:
            gear_numbers.append(number)
    if len(gear_numbers) == 2:
        gear_ratios.append(math.prod([int(i[1]) for i in gear_numbers]))
    ...


print(f'Sum: {sum(gear_ratios)}')
...