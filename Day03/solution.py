def part_1(fp: str) -> int:
    """
    Day 3 part 1 of Advent of Code 2025. Finds the largest subsequence in
    a set of batteries with a length of 2. 

    Args:
        fp (string): input filepath

    Returns:
        Integer: sum of battery joltages (largest subsequences)
    """

    with open(fp) as f:
        total = 0
        for line in f:
            max_1 = -1
            max_2 = -1

            for i, digit in enumerate(line.strip()):
                if (int(digit) > max_1) and (i != len(line.strip()) - 1):
                    max_1 = int(digit)
                    max_2 = -1
                elif (int(digit) > max_2):
                    max_2 = int(digit)
            
            total += max_1 * 10 + max_2
    return total

def part_2(fp:str, num_batteries:int=12) -> int:
    """
    Day 3 part 2 of Advent of Code 2025. Finds the largest subsequence
    in a set of batteries to turn on.

    Args:
        fp (string): input filepath
        num_batteries (integer): number of batteries to turn on (length of subsequence)

    Returns:
        Integer: sum of battery joltages (largest subsequences)
    """

    with open(fp) as f:
        total = 0
        for line in f:
            maxes = {i:-1 for i in range(num_batteries)}

            for i, digit in enumerate(line.strip()):
                # index for batteries that can have new local max
                check_index = len(line.strip()) - i - num_batteries
                if check_index > 0:
                    check_index = 0
                else:
                    check_index = abs(check_index)

                for k, v in maxes.items():
                    if k < check_index:
                        continue
                    if int(digit) > v:
                        maxes[k] = int(digit)

                        # reset maxes after the new local max
                        for j in range(k + 1, num_batteries):
                            maxes[j] = -1
                        break
            
            total += int(''.join([str(maxes[i]) for i in range(num_batteries)]))
            
    return total

if __name__ == '__main__':
    # tests and input filepaths
    test_fp = './tests/test_input.txt'
    input_fp = './tests/input.txt'

    assert part_2(test_fp, 2) == 357
    assert part_2(test_fp) == 3121910778619

    # actual output
    print(part_1(input_fp))
    print(part_2(input_fp))