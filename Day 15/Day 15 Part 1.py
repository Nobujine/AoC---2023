filename = 'Day 15/input.txt'


def decode_hash(input_string:str) -> int:
    output = 0
    for char in input_string:
        output += ord(char)
        output *= 17
        output = output % 256
        ...
    return output


with open(filename, 'r') as f:
    data = f.read().split(',')

scores = [decode_hash(entry) for entry in data]

print(f'Answer: {sum((scores))}')

...