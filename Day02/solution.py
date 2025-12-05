def part_1(fp: str) -> int:
    """
    Day 2 part 1 of Advent of Code 2025. Given a list of ranges,
    see if there are numbers within the range that are some sequence
    of digits repeated twice.

    Args:
        fp (string): input filepath

    Returns:
        Integer: sum of numbers with number sequence repeated twice
    """

    file = ''
    with open(fp) as f:
        file = f.readlines()
    
    ranges = file[0].split(',')
    total = 0

    for ran in ranges:
        # parse ranges
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)

            # odd length can't be duplicated twice
            if num_len % 2 == 1:
                continue
            
            # check for repeat in first and second half
            if str_num[:num_len//2] == str_num[num_len//2:]:
                total += num

    return total

def part_2(fp: str) -> int:
    """
    Day 2 part 2 of Advent of Code 2025. This one was my original solution.
    Given a list of ranges, see if there are numbers within the
    range that are some sequence of digits repeated any number of times.

    Args:
        fp (string): input filepath

    Returns:
        Integer: sum of numbers with number sequence repeated
    """

    file = ''
    with open(fp) as f:
        file = f.readlines()
    
    ranges = file[0].split(',')
    total = 0

    for ran in ranges:
        # parse ranges
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            possible = []

            # check for possible repeated number lengths
            for i in range(1, num_len // 2 + 1):
                if num_len % i == 0:
                    possible.append(i)
            
            for size in possible:
                # flag for if the number is repeated x number of times
                flag = True
                for i in range(0, num_len - size, size):
                    # check sequence in front of current seq
                    if str_num[i:i+size] == str_num[i+size:i+(2*size)]:
                        continue
                    else:
                        flag = False
                if flag:
                    total += num
                    break
            
    return total

def part_2_new(fp: str) -> int:
    """
    Day 2 part 2 of Advent of Code 2025. Given a list of ranges, 
    see if there are numbers within the range that are some sequence of digits 
    repeated any number of times.

    Args:
        fp (string): input filepath
    Returns:
        Integer: sum of numbers with number sequence repeated
    """
    ranges = ''
    total = 0

    with open(fp) as f:
        ranges = f.read().split(',')

    for ran in ranges:
        # parse ranges
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            for i in range(1, num_len // 2 + 1):
                # check for duplication if original number can be assembled
                if (num_len % i == 0) and ((str_num[:i] * (num_len//i)) == str_num):
                    total += num
                    break
            
    return total

if __name__ == '__main__':
    # tests and input filepaths
    fp = './tests/input.txt'
    test_fp = './tests/test_input.txt'
    part_2_test = part_2(test_fp)

    assert part_2_test == 4174379265

    # actual outputs
    print(part_1(fp))
    print(part_2(fp))
    print(part_2_new(fp))