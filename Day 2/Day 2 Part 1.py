# imports
import re

filename = 'Day 2/input.txt'

max_possible = {'red':12, 'green':13, 'blue':14}
colors = ['red', 'green', 'blue']

def possible(line:str) -> bool:
    ...
    for game in line.split(';'):
        for mat in re.findall('([0-9]+) ([a-z]+)', game):
            value = mat[0]
            color = mat[1]
            if max_possible[color] < int(value):
                return False
    return True

possible_games = []
with open(filename, 'r') as f:
    for line in f.readlines():
        game_number = int(re.match('Game ([0-9]+)', line).group(1))
        if possible(line):
            possible_games.append(game_number)
        ...

print(f'Sum: {sum(possible_games)}')
...