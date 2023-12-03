import re

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
        for symbol in re.finditer(r'([^0-9.\n])', line):
            x = symbol.span()[0]
            symbols.append((x,y,symbol.group()[0]))

# Parse for numbers, check adjacent cells        
valid_numbers = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.readlines()):
        for number in re.finditer('([0-9]+)', line):
            x = number.span()[0]
            number_text = number.group()
            positions = [(x+i,y) for i in range(len(number_text))]
            if check_number(positions, symbols):
                valid_numbers.append(int(number_text))

print(f'Sum: {sum(valid_numbers)}')
...