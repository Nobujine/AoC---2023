# Time:      7  15   30
# Distance:  9  40  200

import math

filename = 'Day 6/input.txt'

with open(filename, 'r') as f:
    times = f.readline().split()[1:]
    distance = f.readline().split()[1:]
    # Time / Distance
    races = {int(times[i]):int(distance[i]) for i in range(len(times))}


def calculate_distance(time_held, max_time):
    return (max_time - time_held) * time_held

ways_to_win = []
for max_time, winning_distance in races.items():
    winning_distances = []
    for i in range(max_time):
        distance = calculate_distance(i,max_time)
        if distance > winning_distance:
            winning_distances.append(distance)
    ways_to_win.append(len(winning_distances))

print(f'Output: {math.prod(ways_to_win)}')
...