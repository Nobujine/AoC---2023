filename = 'Day 16/input.txt'

UP =    (0, -1)
DOWN =  (0,  1)
LEFT =  (-1, 0)
RIGHT = (1,  0)

def add_pos(A:tuple, B:tuple)->tuple:
    return tuple(A[i]+B[i] for i in range(min(len(A), len(B))))

def inside_grid(pos:tuple, grid_size:tuple) -> bool:
    for i in [0, 1]:
        if 0 > pos[i] or pos[i] > grid_size[i]:
            return False
    return True

def split_beam(pos:tuple, directions:list, ) -> list:
    output = [[pos, d] for d in directions]
    return output

# Read File
mirrors = {}
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, char in enumerate(line):
            if not char == '.':
                pos = (x, y)
                mirrors[pos] = char
grid_size = (x,y)

def draw(mirrors:dict, grid_size:tuple, energized_tiles:set = set(), beam:tuple = (-1,-1)) -> None:
    lookup_dict = {UP:'^',DOWN: 'v',RIGHT:'>', LEFT:'<'}
    for y in range(grid_size[1]+1):
        line = ''
        for x in range(grid_size[0]+1):
            pos = (x,y)
            char = '.'
            if pos in mirrors:
                char = mirrors[pos]
            if pos in energized_tiles:
                char = '#'
            if pos == beam[0]:
                char = lookup_dict[beam[1]]
            line += char
        print(line)


# Set up initial beam per Da Rules

beams = []
start_pos = (-1,0)
energized_tiles = set()
start_direction = RIGHT
beams.append([start_pos, start_direction])

# iterate beams
closed_list = []
while beams:
    beam = beams.pop()
    if beam in closed_list:
        continue
    closed_list.append(beam)
    pos = add_pos(beam[0], beam[1])  # move beam 1 square
    if inside_grid(pos, grid_size):
        energized_tiles.add(pos)
        #draw(mirrors, grid_size, energized_tiles, [pos, beam[1]])
        if pos not in mirrors:
            beams.append([pos, beam[1]])
        else:
            mirror = mirrors[pos] 
            if mirror == '|' and (beam[1] == RIGHT or beam[1] == LEFT):
                new_beams = split_beam(pos, [UP, DOWN])
                beams += new_beams
            elif mirror == '-' and (beam[1] == UP or beam[1] == DOWN):
                new_beams = split_beam(pos, [LEFT, RIGHT])
                beams += new_beams
            elif mirror == '\\':
                if beam[1] == RIGHT: beams.append([pos,DOWN])
                if beam[1] ==  LEFT:  beams.append([pos,UP])
                if beam[1] ==  UP:    beams.append([pos,LEFT])
                if beam[1] ==  DOWN:  beams.append([pos,RIGHT])
            elif mirror ==  r'/':
                if beam[1] == RIGHT: beams.append([pos,UP])
                if beam[1] ==  LEFT:  beams.append([pos,DOWN])
                if beam[1] ==  UP:    beams.append([pos,RIGHT])
                if beam[1] ==  DOWN:  beams.append([pos,LEFT])

            else:
                beams.append([pos, beam[1]])

#draw(mirrors, grid_size, energized_tiles)
print(f'Answer: {len(energized_tiles)}')
        
...