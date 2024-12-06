import os
import time

def read_data(filepath:str) -> list:
    with open(filepath) as f:
        data = f.read().splitlines()
    return data

def main():
    working_folder = os.path.dirname(os.path.realpath(__file__))
    test_path = os.path.join(working_folder, "test.txt")
    input_path = os.path.join(working_folder, "input.txt")
    test_data = read_data(test_path)
    input_data = read_data(input_path)

    print('\nTest:')
    timer = time.perf_counter()
    print(f"Part 1: {part_1(test_data)}   Time: {time.perf_counter() - timer:.4f}")
    timer = time.perf_counter()
    print(f"Part 2: {part_2(test_data)}   Time: {time.perf_counter() - timer:.4f}")

    print('\nActual Result:')
    timer = time.perf_counter()
    print(f"Part 1: {part_1(input_data)}   Time: {time.perf_counter() - timer:.4f}")
    timer = time.perf_counter()
    print(f"Part 2: {part_2(input_data)}   Time: {time.perf_counter() - timer:.4f}")
    ...

def part_1(data:list) -> int:
    pass

def part_2(data:list) -> int:
    pass

if __name__ == '__main__':
    main()