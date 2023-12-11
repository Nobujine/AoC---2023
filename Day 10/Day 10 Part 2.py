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

filename = 'Day 10/part2_test.txt'

grid = {}
start_position = None
open_tiles = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, tile in enumerate(line):
            pos = (x,y)
            if tile == '.':
                open_tiles.append((x,y))
            else:
                grid[pos] = [add_tuples(pos, con) for con in connections[tile]]
                if tile == 'S':
                    start_position = pos
gridsize = max(x,y)

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

def find_path(graph, start, end) -> bool:
    open_list = [start]
    closed_list = set()
    while open_list:
        node = open_list.pop()
        connections = graph[node] if node in graph else []
        if end in connections:
            return True
        for connection in connections:
            if connection not in closed_list:
                open_list.append(connection) 
        closed_list.add(node)
    return False

pipe = find_cycle(grid, start_position)

NORTH = (0,-1)
SOUTH = (0,1)
EAST = (1,0)
WEST = (-1,0)

def inside(pipe:dict, point:tuple) -> bool:
    # traverse along X axis and count transitions
    y = point[1]
    count = 0
    for x in range((point[0]+1)):
        current_tile = (x, y)
        last_tile = (x-1, y)
        
        transition_out = current_tile not in pipe and last_tile in pipe
        if transition_out and current_tile not in pipe:
            count += 1

        print(f'Tile: {current_tile} inside: {bool(count % 2)}')
    
    return bool(count % 2)
    ...

test = inside(pipe, (5,4))

count = 0
open_tiles = [[tile, inside(pipe, tile)] for tile in open_tiles]
for point in open_tiles:
    if point[1]:
        count += 1

print(f'interior points: {count}')
...

