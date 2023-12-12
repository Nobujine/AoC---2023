
from functools import cache

filename = 'Day 12/test_input.txt'

with open(filename, 'r') as f:
    data = [line.split(' ') for line in f.read().splitlines()]

data = [[grid, [int(x) for x in values.split(',')]] for grid, values in data]

def generate_possibilities(line:str) -> list:
    # generate and return all combinations of lists
    if '?' not in line:
        return []
    
    open_list = []
    closed_list = set()
    line = list(line)
    open_list.append(line)

    while open_list:
        line = open_list.pop()
        if '?' in line:
            unknown = [i for i, char in enumerate(line) if char == '?']    
            for i in unknown:
                for char in ['#', '.']:
                    new_list = line.copy()
                    new_list[i] = char
                    open_list.append(new_list)
        else:
            closed_list.add(''.join(line))
    return list(closed_list)

def solve_line(line:str, values:list) -> list:
    # generate and return all combinations of lists
    @cache
    def evaluate_line(line:str) -> bool:
        if '?' in line:
            raise ValueError('Only solved lines, received: {line}')
        groups = [group for group in line.split('.') if '#' in group]
        if len(groups) != len(values):
            return False
        for i , group in enumerate(groups):
            if len(group) != values[i]:
                return False
        return True

    if '?' not in line:
        return []
    
    open_list = []
    closed_list = set()
    count = 0
    line = list(line)
    open_list.append(line)

    while open_list:
        line = open_list.pop()
        if '?' in line:
            unknown = [i for i, char in enumerate(line) if char == '?']    
            for i in unknown:
                for char in ['#', '.']:
                    new_list = line.copy()
                    new_list[i] = char
                    open_list.append(new_list)
        else:
            line = ''.join(line)
            if line not in closed_list:
                count += 1 if evaluate_line(line) else 0
                closed_list.add(line)
    return count

counts = []
for line in data:
    values = line[1]
    count = solve_line(line[0], values)
    print(f'{line} {count=}')
    counts.append(count)
    ...

print(f'{sum(counts)=}')
...