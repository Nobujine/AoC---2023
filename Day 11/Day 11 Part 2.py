from copy import deepcopy

filename = 'Day 11/input.txt'

galaxies = []
with open(filename, 'r') as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append([x,y])
space_size = (x,y)

# expand 
EXPANSION_RATE = 1_000_000
expanded_galaxies = deepcopy(galaxies)
for xy in [0,1]:
    occupied = [g[xy] for g in galaxies]
    empty_area = []
    for i in range(space_size[xy]):
        if i in occupied:
            continue  # we found a galaxy in this column
        for galaxy_number, galaxy in enumerate(galaxies):
            if galaxy[xy] > i:
                expanded_galaxies[galaxy_number][xy] += EXPANSION_RATE-1
galaxies = expanded_galaxies

def L_distance(A:tuple, B:tuple) -> int:
    return sum([abs(B[i]-A[i]) for i in range(len(A))])

distances = []
for galaxy_number, galaxy_A in enumerate(galaxies):
    for galaxy_B in galaxies[galaxy_number+1:]:
        distance = L_distance(galaxy_A, galaxy_B)
        distances.append(distance)
        # print(f'Pair: {galaxy_A}, {galaxy_B}, dist: {L_distance(galaxy_A, galaxy_B)}')
        
print(f'{len(distances)=}')
print(f'{sum(distances)=}')

...
