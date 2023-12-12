
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
    
def evaluate_line(line:str, values:list) -> bool:
    if '?' in line:
        raise ValueError('Only solved lines, received: {line}')
    groups = [group for group in line.split('.') if '#' in group]
    for i , group in enumerate(groups):
        if len(group) != values[i]:
            return False
    return True
    ...

for line in data:
    values = line[1]
    possibilities = generate_possibilities(line[0])
    evaluated = [evaluate_line(line, values) for line in possibilities]
    count = len([x for x in evaluated if x])
    print(f'{line} {count=}')
    ...

...