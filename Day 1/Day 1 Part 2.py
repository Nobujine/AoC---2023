
word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for i in range(10):
    word_dict[str(i)] = i

filename = 'Day 1/input.txt'

# Collect all numbers for debugging purposes
extracted = []
with open(filename, 'r') as f:
    for line in f.read().splitlines():
        first_numbers = {line.find(num):word_dict[num]  for num in word_dict.keys() if line.find(num)  >= 0}
        last_numbers =  {line.rfind(num):word_dict[num] for num in word_dict.keys() if line.rfind(num) >= 0}
        first = first_numbers[min(first_numbers)]
        last = last_numbers[max(last_numbers)]
        number = int(str(first) + str(last))
        extracted.append(number)
        ...

print(f'sum: {sum(extracted)}')
...