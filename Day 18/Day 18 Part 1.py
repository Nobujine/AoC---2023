filename = 'Day 18/input.txt'

with open(filename, 'r') as f:
    instructions = f.read().splitlines()
instructions = [line.split() for line in instructions]

UP =    (0, -1)
DOWN =  (0,  1)
LEFT =  (-1, 0)
RIGHT = (1,  0)
direction = {'R':RIGHT, 'L': LEFT, 'U':UP, 'D':DOWN}

def add_tuples(A:tuple, B:tuple)->tuple:
    return tuple(B[i]+A[i] for i in range(min(len(A), len(B))))

def is_inside(pos:tuple, perimiter:set, x_min:int)->bool:
    if pos in perimiter:
        return False
    count = 0
    for x in range(x_min, pos[0]):
        if (x, pos[1]) in perimiter:
            if (x-1, pos[1]) not in perimiter:
                count += 1
    return bool(count % 2)

def draw(y_min:int, y_max:int, x_min:int, x_max:int, perimiter:set=set(), interior:set=set())->None:
    y_max = min(30, y_max)
    x_max = min(10, x_max)
    for y in range(y_min, y_max):
        line = ''
        for x in range(x_min,x_max):
            char = '.'
            if (x,y) in perimiter:
                char = '#'
            if (x,y) in interior:
                char = '+'
            line += char
        print(line)


start_pos = (0,0)
perimiter = set()
perimiter.add(start_pos)
pos = start_pos

x_max = 0
x_min = 0
y_max = 0
y_min = 0

# build perimiter
for ins in instructions:
    for i in range(int(ins[1])):
        pos = add_tuples(pos, direction[ins[0]])
        perimiter.add(pos)
        x_max = max(x_max, pos[0])
        x_min = min(x_min, pos[0])
        y_max = max(y_max, pos[1])
        y_min = min(y_min, pos[1])

#draw(y_min,y_max+1,x_min,x_max+1, perimiter)
...

count = len(perimiter)
interior = set()
for y in range(y_min, y_max):
    for x in range(x_min, x_max):
        pos = (x,y)
        if is_inside(pos, perimiter, x_min):
            count += 1
            interior.add(pos)

draw(y_min,y_max+1,x_min,x_max+1, perimiter, interior)

print(f'Answer: {count}')
...