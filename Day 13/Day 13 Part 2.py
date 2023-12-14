
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

def rotate_grid(grid:list) -> list:
    output = []
    for y in range(len(grid[0])):
        output.append(''.join([line[y] for line in grid]))
    return output

def find_reflection(grid:list, original_reflection:int = -1) -> int:
    for i in range(1, len(grid[0])):
        if test_grid(grid, i):
            if i != original_reflection:
                return i
    rotated = rotate_grid(grid)
    for i in range(1, len(rotated[0])):
        if test_grid(rotated, i):
            if i*100 != original_reflection:
                return i*100
    return False

def fix_smudges(grid:list, original_reflection:int):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            new_grid = grid.copy()
            char = list(grid[y])[x]
            char = '.' if char == '#' else '#'  # flip the character
            new_line = list(grid[y])
            new_line[x] = char
            new_grid[y] =   ''.join(new_line)
            position = find_reflection(new_grid, original_reflection)
            if position and not position == original_reflection:
                return position
    return False

# find answers for part 1
output = {}
rot_found_flag = False
for grid_no, grid in enumerate(data):
    position = find_reflection(grid)
    if position:
        output[grid_no] = position

print(f'Part 1: {sum(output.values())}')

part_2 = []
for grid_no, grid in enumerate(data):
    original_reflection = output[grid_no]
    position = fix_smudges(grid, original_reflection)
    if position:
        part_2.append([grid_no,position])
        ...

print(f'Part 2: {sum(x[1] for x in part_2)}')
...