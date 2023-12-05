filename = 'Day 5/input.txt'

with open(filename, 'r') as f:
    almanac = f.read()
    sections = [x.split('\n') for x in almanac.split('\n\n')]

# process seed line
seeds = [int(x) for x in sections.pop(0)[0].split()[1:]]

# process almanac sections
sections = [x[1:] for x in sections]  # remove header, they are sequentially listed
sections = [[[int(z) for z in y.split()] for y in x] for x in sections]  # Convert everything to list of numbers

def convert_number(number:int, section:list) -> int:
    # Destination Source Range_Length
    for map_range in section:
        if map_range[1] <= number <= map_range[1]+map_range[2]:
            return number + map_range[0] - map_range[1]
    return number

# convert from seed through all the sections
for section in sections:
    seeds = [convert_number(seed, section) for seed in seeds]

print(f'Minimum Location: {min(seeds)}')

...