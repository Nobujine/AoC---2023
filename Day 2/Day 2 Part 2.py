# imports
import re
import math

filename = 'Day 2/input.txt'

max_possible = {'red':12, 'green':13, 'blue':14}
colors = ['red', 'green', 'blue']

def get_requirement(line:str) -> bool:
    ...
    output_dict = {color:0 for color in colors}
    for game in line.split(';'):
        for mat in re.findall('([0-9]+) ([a-z]+)', game):
            value = mat[0]
            color = mat[1]
            output_dict[color] = max(output_dict[color], int(value))
    return output_dict

requirements = []
with open(filename, 'r') as f:
    for line in f.readlines():
        game_number = int(re.match('Game ([0-9]+)', line).group(1))
        required = get_requirement(line)
        power = math.prod(required.values())
        requirements.append(power)
        ...

print(f'Sum: {sum(requirements)}')
...