import re

filename = 'Day 1/input.txt'
output = 0
with open(filename, 'r') as f:
    for line in f.read().splitlines():
        numbers = re.findall('[0-9]', line)
        first = numbers[0]
        last = numbers[-1]
        number = int(first + last)
        output += number
        ...

print(f'sum: {output}')