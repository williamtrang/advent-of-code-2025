from operator import itemgetter

def part_1(fp: str) -> int:
    """
    Day 5 part 1 of Advent of Code 2025. For each ingredient that is
    available, check if it is fresh by checking the fresh ingredient ranges.
    Returns the count of available fresh produce.
    
    Args:
        fp (string): input filepath

    Returns:
        Integer: count of fresh ingredients out of available
    """

    with open(fp) as f:
        db = f.readlines()

        # parse fresh produce ranges
        fresh_ranges = db[:db.index('\n')]
        fresh_ranges = [list(map(int, fresh.split('-'))) for fresh in fresh_ranges]

        # available produce IDs
        available = db[db.index('\n') + 1:]
        fresh_count = 0

        for ingredient_id in available:
            for fresh in fresh_ranges:
                low, high = fresh
                if int(ingredient_id) in range(low, high + 1): # check if ingredient is fresh
                    fresh_count += 1
                    break
    
        return fresh_count

def part_2(fp: str) -> int:
    """
    Day 5 part 2 of Advent of Code 2025. Builds a list of "fresh produce"
    ingredient IDs and counts the total number of IDs. To do this, sort the
    ranges of product IDs and combine the overlapping ones, then get the size
    of all the ranges together.

    Args:
        fp (string): input filepath

    Returns:
        Integer: Count of ingredient IDs that are fresh
    """

    with open(fp) as f:
        db = f.readlines()

        # parse fresh produce ranges
        fresh_ranges = db[:db.index('\n')]
        fresh_ranges = [list(map(int, fresh.split('-'))) for fresh in fresh_ranges]

        fresh_ranges_sorted = sorted(fresh_ranges, key=itemgetter(0, 1))
        fresh_ranges_merged = [fresh_ranges_sorted[0]]
        fresh_id_count = 0

        for fresh in fresh_ranges_sorted:
            low, high = fresh
            fresh_range_high = fresh_ranges_merged[-1][1]

            # update fresh produce ranges
            if low > fresh_range_high:
                fresh_ranges_merged.append(fresh)
            elif high > fresh_range_high:
                fresh_ranges_merged[-1][1] = high
        
        # count number of fresh ingredient IDs
        for ran in fresh_ranges_merged:
            fresh_id_count += ran[1] - ran[0] + 1

        return fresh_id_count

if __name__ == '__main__':
    # tests and input filepaths
    test_fp = './tests/test_input.txt'
    test_fp_2 = './tests/test_input_2.txt'
    test_fp_3 = './tests/test_input_3.txt'
    test_fp_4 = './tests/test_input_4.txt'
    input_fp = './tests/input.txt'

    assert part_1(test_fp) == 3
    assert part_2(test_fp) == 14
    assert part_2(test_fp_2) == 10
    assert part_2(test_fp_3) == 10
    assert part_2(test_fp_4) == 31

    # actual output
    print(part_1(input_fp))
    print(part_2(input_fp))
