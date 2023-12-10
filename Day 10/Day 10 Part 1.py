filename = 'Day 10/test_input.txt'

grid = {}
start_position = None
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, tile in enumerate(line):
            if tile != '.':
                grid[(x,y)] = tile 
            if tile == 'S':
                start_position = (x,y)

def L_distance(A:tuple, B:tuple) -> int:
    return max(B[0]-A[0], B[1]-A[1])



...