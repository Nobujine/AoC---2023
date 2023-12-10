import networkx as nx

# (x,y)
NORTH = (0,-1)
SOUTH = (0,1)
EAST = (1,0)
WEST = (-1,0)

connections = {
    '|': [NORTH, SOUTH],
    '-': [EAST, WEST],

    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
    'S': []  # Start position
    }

def add_tuples(A:tuple, B:tuple) -> tuple:
    return (A[0]+B[0], A[1]+B[1])

filename = 'Day 10/input.txt'

grid = {}
start_position = None
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, tile in enumerate(line):
            if tile != '.':
                pos = (x,y)
                grid[pos] = [add_tuples(pos, con) for con in connections[tile]]
                if tile == 'S':
                    start_position = pos

# add starting connections
for node, connections in grid.items():
    if start_position in connections:
        grid[start_position].append(node)

def find_cycle(graph, start) -> set:
    open_list = [start]
    closed_list = set()
    while open_list:
        node = open_list.pop()
        connections = graph[node]
        for connection in connections:
            if connection not in closed_list:
                open_list.append(connection) 
        closed_list.add(node)
    return closed_list

cycle = find_cycle(grid, start_position)

print(f'Answer: {len(cycle)//2}')

...