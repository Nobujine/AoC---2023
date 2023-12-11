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

#filename = 'Day 10/part2_test.txt'
filename = 'Day 10/input.txt'

grid = {}
start_position = None
vertical_bars = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, tile in enumerate(line):
            pos = (x,y)
            if tile == '|' or tile == 'J' or tile == 'L' or tile == 'S':
                vertical_bars.append(pos)
            if tile == '.':
                ...
            else:
                grid[pos] = [add_tuples(pos, con) for con in connections[tile]]
                if tile == 'S':
                    start_position = pos
gridsize = (x,y)

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

pipe = find_cycle(grid, start_position)

def inside(point:tuple, bars:set) -> bool:
    y = point[1]
    count = 0
    for x in range(point[0]):
        check_point = (x,y)
        if check_point in vertical_bars:
            count += 1
        #print(f'Tile: {check_point} inside: {bool(count % 2)}')
    return bool(count % 2)

# generate a list of all tiles that aren't the pipe itself
open_tiles = []
for y in range(gridsize[1]):
    for x in range(gridsize[0]):
        tile = (x,y)
        if tile not in pipe:
            open_tiles.append(tile)

vertical_bars = set(bar for bar in vertical_bars if bar in pipe)
open_tiles = [[tile, inside(tile, vertical_bars)] for tile in open_tiles]

count = 0
for point in open_tiles:
    if point[1]:
        count += 1

print(f'interior points: {count}')
# not 458
# 449 per reddit
# I fucking forgot the S counts as a pipe, that fixed it. jesus
...