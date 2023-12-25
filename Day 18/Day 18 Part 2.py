filename = 'Day 18/input.txt'

def decode(hex_number:str)-> list:
    direction = {'0':'R', '1':'D', '2':'L', '3':'U'}
    number = int(hex_number[2:7],16)
    return [direction[hex_number[-2]], number]
    ...

# test = decode('(#70c710)') # should be R 461937
...

with open(filename, 'r') as f:
    instructions = f.read().splitlines()
instructions = [line.split() for line in instructions]
instructions = [decode(ins[2]) for ins in instructions]
...



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
perimiter = 0
pos = start_pos

points = []
# build perimiter
for ins in instructions:
    d = direction[ins[0]]
    distance = int(ins[1])
    d = (d[0]*distance, d[1]*distance)
    pos = add_tuples(pos, d)
    perimiter += distance
    points.append(pos)   


def area(points:list)->int:
    #shoelace theorem
    results = []
    for i in range(-1, len(points)-1):
        a = points[i]
        b = points[i+1]
        results.append(a[0]*b[1] - a[1]*b[0])
        ...
    output = sum(results)/2
    return output

def picks(area:int, b:int)->int:
    return area-(b/2)+1

#test = shoelace([(1,6),(3,1),(7,2), (4,4), (8,5)])
a = area(points)
interior_points = picks(a, perimiter)
answer = interior_points + perimiter

print(f'Answer: {int(answer)}')
...