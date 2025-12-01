import argparse

from typing import Sequence
from utils import read_file

def part_1(data: Sequence[str]) -> int:
    """
    Day 1 part 1 of Advent of Code 2025. Counts the number of times
    the dial ends on 0 after a series of moves.

    Args:
        data (Sequence): Array-like of dial rotations
    Returns:
        Integer: count of times dial ends at 0
    """

    dial = 50
    cnt = 0

    for combo in data:
        direction = combo[0] # L or R
        num = int(combo[1:].strip())

        if direction == 'L': # left
            dial = (dial - num) % 100
        else: # right
            dial = (dial + num) % 100
        
        if dial == 0:
            cnt += 1

    return cnt

def part_2(data: Sequence[str]) -> int:
    """
    Day 1 part 2 of Advent of Code 2025. Count the number of times 0
    is passed.

    Args:
        data (Sequence): Array-like of dial rotations
    Returns:
        Integer: count of times 0 is passed on the dial
    """
    
    dial = 50
    cnt = 0

    for combo in data:
        direction = combo[0] # L or R
        num = int(combo[1:].strip())
        init_zero = dial == 0

        if direction == 'L': # left
            dial = (dial - num)
            if (dial < 0) and init_zero:
                cnt -= 1
        else: # right
            dial = (dial + num)
        
        cnt += abs(dial // 100)

        if dial == 0:
            cnt += 1

        if dial < 0 and dial % 100 == 0:
            cnt += 1

        dial %= 100

    return cnt

if __name__ == '__main__':
    # tests
    test_1_fp = './tests/test_input.txt'
    test_2_fp = './tests/test_input_2.txt'
    test_1 = read_file(test_1_fp)
    test_2 = read_file(test_2_fp)

    assert part_1(test_1) == 3
    assert part_1(test_2) == 1
    assert part_2(test_1) == 6
    assert part_2(test_2) == 3

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--fp', default='./tests/input.txt', type=str, help='filepath to process')
    args = parser.parse_args()
    fp = args.fp

    # read input file
    file = read_file(fp)

    # give output
    print(part_1(file))
    print(part_2(file))
