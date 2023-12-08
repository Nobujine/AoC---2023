import math

def main():
    filename = 'Day 8/input.txt'
    with open(filename, 'r') as f:
        instructions = f.readline().split('\n')[0]
        f.readline()  # blank line in input
        network = f.readlines()
        network = [line.split('\n')[0] for line in network]
        network = [line.split('=') for line in network]
        network = {start.strip():[c.strip() for c in connection.replace('(', '').replace(')','').strip().split(',')] for start,connection in network}
    current_position = [pos for pos in network if pos[-1] == 'A']

    directions = {'R':1, 'L':0}
    steps = 0
    # loop until we reach the exit
    loop_location = []
    while current_position:
        index = steps % len(instructions)
        next_step = directions[instructions[index]]
        current_position = [network[pos][next_step] for pos in current_position]
        steps += 1
        
        # Get a list of where we land at Z
        for pos in current_position:
            if pos[-1] == 'Z':
                loop_location.append(steps)
                current_position.remove(pos)

    # Get the lowest common multiple of the locations where we are at Z
    print(f'Output: {math.lcm(*loop_location)}')
    ...

if __name__ == '__main__':
    main()