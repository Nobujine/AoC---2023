filename = 'Day 9/input.txt'

with open(filename, 'r') as f:
    history = f.readlines()
history = [[int(y) for y in x.split()] for x in history]

def differences(x:list) -> list:
    return [x[i+1] - x[i] for i in range(len(x)-1)]

def extrapolate(numbers:list) -> int:
    # recursive function, find the differences between all values, if all values are 0 return and add up
    # calculate differences
    d = differences(numbers)
    if len(set(d)) == 1:
        return d[-1] + numbers[-1]
    else:
        new_number = extrapolate(d)
        return new_number + numbers[-1]
    
history = [list(reversed(h)) for h in history]  # lol come on 2ez4me
next_digits = [extrapolate(line) for line in history]

print(f'Sum of next digits: {sum(next_digits)}')

...