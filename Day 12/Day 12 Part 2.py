from functools import cache

filename = 'Day 12/test_input.txt'

with open(filename, 'r') as f:
    data = [line.split(' ') for line in f.read().splitlines()]

data = [[grid, [int(x) for x in values.split(',')]] for grid, values in data]

data = [[(line[0]+'?')*5,line[1]*5] for line in data]


def naive_solve_line(line:str, values:list) -> int:
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
            i = unknown.pop()
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

def evaluate_line(line:str, values:list) -> bool:
    if '?' in line:
        raise ValueError('Only solved lines, received: {line}')
    groups = [group for group in line.split('.') if '#' in group]
    if len(groups) != len(values):
        return False
    for i , group in enumerate(groups):
        if len(group) != values[i]:
            return False
    return True

output = []
for line in data:
    output.append([line[0], naive_solve_line(*line)])


print(f'Answer: {sum([x[1] for x in output])}')

...