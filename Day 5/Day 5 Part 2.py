filename = 'Day 5/input.txt'

with open(filename, 'r') as f:
    almanac = f.read()
    sections = [x.split('\n') for x in almanac.split('\n\n')]

# process seed line
seeds = [int(x) for x in sections.pop(0)[0].split()[1:]]

# Part 2 
# store seeds as ranges, operate on those ranges
seed_ranges = []
for i in range(0,len(seeds),2):
    seed_ranges.append({'start':seeds[i], 'stop':seeds[i]+seeds[i+1]})
...

# process almanac sections
sections = [x[1:] for x in sections]  # remove header, they are sequentially listed
sections = [[[int(z) for z in y.split()] for y in x] for x in sections]  # Convert everything to list of numbers

def convert_number(number:int, section:list) -> int:
    # Destination Source Range_Length
    for map_range in section:
        if map_range[1] <= number <= map_range[1]+map_range[2]:
            return number + map_range[0] - map_range[1]
    return number

def convert_map_range(map_range:list, numbers:list) -> list:
    # Destination Source Range_Length
    offset = map_range[0] - map_range[1]
    mapping_set = set(map_range[1]+j for j in range(map_range[2]))
    new_numbers = []
    unchanged = []
    for number in numbers:
        if number in mapping_set:
            new_numbers.append(number+offset)
        else:
            unchanged.append(number)
    return new_numbers, unchanged
    ...

def convert_seed_ranges(seed_ranges:list, map_range:list) -> list:
    # for 
    ...

# convert from seed through all the sections
new_seeds = []
for section in sections:
    all_changed_seeds = set()
    for map_range in section:
        new_seeds, seeds = convert_map_range(map_range, seeds)
        all_changed_seeds = all_changed_seeds | set(seed for seed in new_seeds if seed not in all_changed_seeds)
        ...
    seeds += all_changed_seeds
    ...
# for section in sections:
#     seeds = [convert_number(seed, section) for seed in seeds]

print(f'Minimum Location: {min(seeds)}')

...