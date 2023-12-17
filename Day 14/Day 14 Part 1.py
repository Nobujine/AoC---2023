filename = 'Day 14/input.txt'


def split_numbers(blocks:list, rocks:list, xy:int, reverse:bool) -> list:
    sorted_rocks = {}
    closed_list = set()
    blocks = [block[xy-1] for block in blocks]
    blocks.sort(reverse=reverse)
    rocks = [rock[xy-1] for rock in rocks]
    for block in blocks:
        sorted_rocks[block] = []
        for rock in rocks:
            if rock > block and rock not in closed_list:
                sorted_rocks[block].append(rock)
                closed_list.add(rock)

    new_rocks = []
    for key, value in sorted_rocks.items():
        for i in range(len(value)):
            new_rocks.append(key+i+1)
    ...
    return new_rocks
        
def roll_rocks(blocks:list, rocks:set, direction:tuple) -> set:
    # returns new list of round rocks


    xy = direction[0]
    reverse = direction[1]

    row_or_col = set(rock[xy] for rock in rocks)
    for i in row_or_col:
        relevant_blocks = [block for block in blocks if block[xy] == i]
        relevant_rocks  = [rock for rock  in rocks  if rock[xy]  == i]
        new_rocks = split_numbers(relevant_blocks, relevant_rocks, xy, reverse)

        # remove all rocks from rocks list
        for old_rock in relevant_rocks:
            rocks.remove(old_rock)
        # add new rocks to rock list
        for new_value in new_rocks:
            new_rock = [0,0]
            new_rock[xy] = i
            new_rock[xy-1] = new_value
            new_rock = tuple(new_rock)
            rocks.add(new_rock)
    
    return rocks

def main():
    # xy, reverse
    NORTH = (0, True)
    SOUTH = (0, False)
    EAST =  (1, True)
    WEST =  (1, False)

    blocks = []
    round_rocks = set()
    with open(filename, 'r') as f:
        
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                pos = (x,y)
                match char:
                    case '#': 
                        blocks.append(pos)
                    case 'O':
                        round_rocks.add(pos)
                    case _:
                        pass
        # create blocks around the outside to stop rolling
        for i in range(x):
            blocks.append((i,-1))
            blocks.append((i, y+1))
        for i in range(y):
            blocks.append((-1,i))
            blocks.append((x+1, i))
    row_count = y+1

    round_rocks = roll_rocks(blocks, round_rocks, NORTH)
    score = sum([row_count - rock[1] for rock in round_rocks])

    print(f'Answer: {score}')
    ...

if __name__ == '__main__':
    main()
    ...
