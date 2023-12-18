import re

filename = 'Day 15/input.txt'


def decode_hash(input_string:str) -> int:
    output = 0
    for char in input_string:
        output += ord(char)
        output *= 17
        output = output % 256
        ...
    return output

def determine_focusing_power(boxes:dict) -> int:
    output = []
    for box_id, lenses in boxes.items():
        for position, lens in enumerate(lenses.values()):
            focusing_power = (box_id+1) * lens * (position+1)
            output.append(focusing_power)
            ...
    return sum(output)
        

with open(filename, 'r') as f:
    data = f.read().split(',')

boxes = {i:{} for i in range(256)}
for entry in data:
    entry = re.split('[=-]', entry)
    id = decode_hash(entry[0])
    if entry[1]: # = in string
        boxes[id][entry[0]] = int(entry[1])
    else:
        boxes[id].pop(entry[0], '')
    ...

test = determine_focusing_power(boxes)

...