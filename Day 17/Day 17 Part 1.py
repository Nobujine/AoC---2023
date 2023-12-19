

filename = 'Day 17/test_input.txt'



class Grid:
    def __init__(self) -> None:
        self.tiles = {}
        self.size = None
    
    def inside_grid(self, pos:tuple) -> bool:
        for i in [0, 1]:
            if 0 > pos[i] or pos[i] > self.size[i]:
                return False
        return True
    
    @staticmethod
    def add_tuples(A:tuple, B:tuple) -> tuple:
        return tuple(B[i]+A[i] for i in range(min(len(A), len(B))))
    
    @staticmethod
    def subtract_tuples(A:tuple, B:tuple) -> tuple:
        return tuple(B[i]-A[i] for i in range(min(len(A), len(B))))

class Node:
    def __init__(self, pos:tuple, value:int) -> None:
        self.pos = pos
        self.value = value

class Cycler:
    def __init__(self, data:list) -> None:
        self.data=data

    def get(self, index):
        return self.data[index%len(self.data)]
    
    def locate(self, value) -> int:
        return self.data.index(value)

def determine_possibilities(path:tuple) -> list:
    UP =    (0, -1)
    DOWN =  (0,  1)
    LEFT =  (-1, 0)
    RIGHT = (1,  0)
    directions = Cycler([RIGHT, DOWN, LEFT, UP])

    # at start position
    if len(path) == 1:  
        return [RIGHT, DOWN]

    # for any other position
    direction = Grid.subtract_tuples(path[-2].pos,path[-1].pos)
    index = directions.locate(direction)
    new_directions = [index-1, index+1, index]
    if len(path) >= 3:
        if check_straight_line(path):
            new_directions.remove(index)
    new_directions = [directions.get(index) for index in new_directions]
    return new_directions

def check_straight_line(path:list)->bool:
    # returns true if the last 3 steps were in a straight line
    directions = set(Grid.subtract_tuples(path[-1-i].pos,path[-i].pos) for i in range(1,3))
    if len(directions) == 1:
        return True
    return False
    ...

def score(node:Node, end:tuple) -> int:
    return node.value + max(end[0]-node.pos[0], end[1]-node.pos[1])

def pathfind(grid:Grid, start:Node, end:tuple) -> list:
    # returns a list of node objects
    open_list = [[start]]
    closed_list = []

    while open_list:
        open_list.sort(key=lambda x:score(x[-1], end))
        path = open_list.pop(0)
        if path[-1].pos == end:
            return path
        closed_list.append(path)
        new_dirs = determine_possibilities(path)
        for direction in new_dirs:
            pos = grid.add_tuples(path[-1].pos, direction)
            if grid.inside_grid(pos):
                value = grid.tiles[pos] + path[-1].value
                new_path = path.copy()
                new_path.append(Node(pos, value))
                if new_path not in closed_list:
                    open_list.append(new_path)
        ...

def main():
    # Read file input
    grid = Grid()
    with open(filename, 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, value in enumerate(line):
                pos = (x,y)
                grid.tiles[pos] = int(value)
    grid.size = (x,y)

    start_pos = (0,0)
    start = Node(start_pos, grid.tiles[start_pos])
    end = grid.size  # bottom right corner, per Da Rules
    path = pathfind(grid, start, end)
    ...

if __name__ == '__main__':
    main()
    ...