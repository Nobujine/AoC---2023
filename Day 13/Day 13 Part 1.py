
filename = 'Day 13/input.txt'
with open(filename, 'r') as f:
    data = f.read().split('\n\n')

data = [d.splitlines() for d in data]  # split each grid up

def test_reflection(line:str, position:int) -> bool:
    # split line
    side_A = line[:position:]
    side_B = line[position::]

    # Reverse side A
    side_A = side_A[::-1]

    # get the first x characters
    split = min(len(side_A), len(side_B))
    side_A = side_A[:split:] 
    side_B = side_B[:split:]

    if side_A == side_B:
        return True
    return False

def test_grid(grid:list, position:int) -> bool:
    for line in grid: # test each line
        if not test_reflection(line, position):
            return False
    return True

def find_reflection(grid:list) -> int:
    for i in range(1, len(grid[0])):
        if test_grid(grid, i):
            return i
    return False

def rotate_grid(grid:list) -> list:
    output = []
    for y in range(len(grid[0])):
        output.append(''.join([line[y] for line in grid]))
    return output


output = []
rot_found_flag = False
for grid_no, grid in enumerate(data):
    position = find_reflection(grid)
    if position:
        output.append([grid_no, position])
    else:
        position = find_reflection(rotate_grid(grid))
        if position:
            output.append([grid_no, position*100])

print(f'Answer: {sum(o[1] for o in output)}')
...