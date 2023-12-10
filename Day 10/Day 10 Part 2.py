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

new_grid = {}
for y in range(0, (gridsize*2)+5):
    for x in range(0, (gridsize*2)+5):
        connections = [add_tuples((x,y), d) for d in [NORTH, SOUTH, EAST, WEST]]
        connections = [c for c in connections if (c[0] >= 0 and c[1] >= 0)]
        new_grid[(x,y)] = connections

for tile in grid:
    tile = tuple(x*2 for x in tile)
    new_grid[tile] = []

count = 0
enclosed_tiles = []
for tile in open_tiles:
    tile = tuple(x*2 for x in tile)
    if not find_path(new_grid, tile, (0,0)):
        enclosed_tiles.append(tile)



...