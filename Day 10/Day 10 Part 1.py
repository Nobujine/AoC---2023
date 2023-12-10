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

g = nx.Graph()
for n in grid.keys():
    g.add_node(n)
    

for start, connections in grid.items():
    for end in connections:
        if end in grid:
            g.add_edge(start, end)

node = g.nodes[start_position]

# Start at (15, 54)
cycle = nx.find_cycle(g, source=start_position)

print(f'Cycle Length: {len(cycle)}')
print(f'Answer: {int(len(cycle)/2)}')
...