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
    seed_ranges.append([seeds[i], seeds[i]+seeds[i+1]])
...

# process almanac sections
sections = [x[1:] for x in sections]  # remove header, they are sequentially listed
sections = [[[int(z) for z in y.split()] for y in x] for x in sections]  # Convert everything to list of numbers

def convert_two_ranges(input_range, map_range) -> list:
    # Return list of new ranges
    # wholly covered
    offset = map_range[0] - map_range[1]
    map_range = [map_range[1], map_range[1]+map_range[2]]
    # Total overlap [10,15], [0,0,25]
    if input_range[0] >= map_range[0] and input_range[1] <= map_range[1]:
        return [[[x+offset for x in input_range]], []] # [10,15], []
    # 3 <= 4 <= 5
    high_intersection = input_range[0] <= map_range[0] <= input_range[1] 
    low_intersection =  input_range[0] <= map_range[1] <= input_range[1]
    # Map inside [0,10], [1,1,5]
    if high_intersection and low_intersection:
        split_range_A = [input_range[0],      map_range[0]-1]
        mapped_range =  [map_range[0]+offset, map_range[1]+offset]
        split_range_B = [map_range[1]+1,        input_range[1]]
        return [[mapped_range],[split_range_A, split_range_B]] # [1,6], [[0,0], [7,10]]
    # low end intersection [10,20], [0,0,15]
    if low_intersection:
        mapped_range = [input_range[0]+offset, map_range[1]+offset-1]
        split_range =  [map_range[1], input_range[1]]
        return  [[mapped_range], [split_range]] # [10,14], [[15,20]]
    # high end intersection [0,10], [5,5,10]
    if high_intersection:
        split_range = [input_range[0],       map_range[0]-1]
        mapped_range = [map_range[0]+offset, input_range[1]+offset]
        return [[mapped_range], [split_range]] # [5,10], [[0,4]]
    # no intersection [0,10], [20,20,20]
    return [[],[input_range]] # [], [[0,10]]

# convert from seed through all the sections
mapped, not_mapped = convert_two_ranges([57,70], [49,53,8])
...

for section in sections:
    mapped_ranges = []
    for map_range in section: 
        unmapped_ranges = []
        for seed_range in seed_ranges:
            mapped, not_mapped = convert_two_ranges(seed_range, map_range)
            mapped_ranges += mapped
            unmapped_ranges += not_mapped
        seed_ranges = unmapped_ranges
    seed_ranges = mapped_ranges + unmapped_ranges

low_end = [seed_range[0] for seed_range in seed_ranges]
print(f'Min: {min(low_end)}')
...