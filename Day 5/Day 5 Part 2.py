filename = 'Day 5/test_input.txt'

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
    # Total overlap
    if input_range[0] >= map_range[0] and input_range[1] <= map_range[1]:
        return [[x+offset for x in input_range]]
    # 3 <= 4 <= 5
    high_intersection = input_range[0] <= map_range[0] <= input_range[1] 
    low_intersection =  input_range[0] <= map_range[1] <= input_range[1]
    # Map inside [0,10], [1,1,5]
    if high_intersection and low_intersection:
        split_range_A = [input_range[0],      map_range[0]-1]
        mapped_range =  [map_range[0]+offset, map_range[1]+offset]
        split_range_B = [map_range[1]+1,        input_range[1]]
        return [split_range_A, mapped_range, split_range_B] # [0,0], [1,6], [7,10]
    # low end intersection [10,20], [0,0,15]
    if low_intersection:
        mapped_range = [input_range[0]+offset, map_range[1]+offset-1]
        split_range =  [map_range[1], input_range[1]]
        return  [mapped_range, split_range] # [10+,14+], [15,20]
    # high end intersection [0,10], [5,5,10]
    if high_intersection:
        split_range = [input_range[0],       map_range[0]-1]
        mapped_range = [map_range[0]+offset, input_range[1]+offset]
        return [split_range, mapped_range] # [0,4] , [5,10]
    # no intersection [0,10], [20,20,20]
    return [input_range] # [0,10]

# convert from seed through all the sections
test = convert_two_ranges([0,10], [1,1,5])
...
seed_ranges = [[82,82]]
for section in sections:
    converted_ranges = []
    for i, seed_range in enumerate(seed_ranges.copy()):
        for map_range in section: 
            new_ranges = convert_two_ranges(seed_range, map_range)
            converted_ranges += new_ranges
    seed_ranges = converted_ranges
    ...
low_end = [seed_range[0] for seed_range in seed_ranges]

print(f'Min: {min(low_end)}')
...