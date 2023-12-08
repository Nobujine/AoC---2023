filename = 'Day 8/test_input.txt'

with open(filename, 'r') as f:
    instructions = f.readline().split('\n')[0]
    f.readline()  # blank line in input
    network = f.readlines()
    network = [line.split('\n')[0] for line in network]
    network = [line.split('=') for line in network]
    network = {start.strip():[c.strip() for c in connection.replace('(', '').replace(')','').strip().split(',')] for start,connection in network}

dir = {'R':1, 'L':0}
# loop until we reach the exit
i = 0
current_position = 'AAA'
while True:
    index = i % len(instructions)
    next_step = instructions[index]
    current_position = network[next_step]
...