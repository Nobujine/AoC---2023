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
    
    @staticmethod
    def L_distance(A:tuple, B:tuple) -> int:
        return max(B[0]-A[0], B[1]-A[1])

class Node:
    def __init__(self, pos:tuple, value:int) -> None:
        self.pos = pos
        self.value = value

def determine_possibilities(path:tuple) -> list:
    UP =    (0, -1)
    DOWN =  (0,  1)
    LEFT =  (-1, 0)
    RIGHT = (1,  0)
    DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

    if len(path) == 1:  # at start position
        value = path[0].value
        return [Node(RIGHT, value), Node(DOWN, value)]
    if 3 > len(path) > 1: # less than 3 moves 
        direction = Grid.subtract_tuples(path[-2].pos,path[-1].pos)
    if len(path) >= 3:  # more than 3 moves, start checking 
        ...
    ...

def pathfind(grid:Grid, start:Node, end:tuple) -> list:
    # returns a list of node objects
    path = []
    path.append(start)
    path.append(Node((0,1),1))
    path.append(Node((0,2),2))

    test = determine_possibilities(path)
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

    start = Node((0,0), 0)
    end = grid.size  # bottom right corner, per Da Rules
    path = pathfind(grid, start, end)
    ...

if __name__ == '__main__':
    main()
    ...