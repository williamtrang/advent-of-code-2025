def part_1(fp:str) -> int:
    """
    Day 4 part 1 of Advent of Code 2025. Gets the total number
    of removable boxes. Removable box is defined as a box with
    fewer than 4 adjacent boxes.

    Args:
        fp (string): input filepath

    Returns:
        Integer: total number of removable boxes
    """
        
    with open(fp) as f:
        grid = f.readlines()
        accessible = 0

        for i, line in enumerate(grid):
            line = line.strip()
            for j, spot in enumerate(line):
                # boxes are marked with @
                if spot == '@':
                    check_spots = [(i-1, j), (i+1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)] # all adjacent spots
                    adj = 0
                    for check in check_spots:
                        x = check[0]
                        y = check[1]

                        # out of bounds check
                        if (x < 0) or (y < 0) or (y >= len(line)) or (x >= len(grid)):
                           continue
                        if grid[x][y] == '@':
                            adj += 1
                    if adj < 4:
                        accessible += 1
    
    return accessible

def part_2(fp:str) -> int:
    """
    Day 4 part 2 of Advent of Code 2025. Gets the total number
    of removable boxes if removable boxes are actually removed.

    Args:
        fp (string): input filepath

    Returns:
        Integer: total number of removable boxes
    """

    with open(fp) as f:
        grid = f.readlines()
        grid = [list(line.strip()) for line in grid]
        accessible = 0
        to_add = -1

        while to_add != 0:
            to_add = 0

            for i, line in enumerate(grid):
                for j, spot in enumerate(line):
                    # boxes are marked with @
                    if spot == '@':
                        check_spots = [(i-1, j), (i+1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)] # all adjacent spots
                        adj = 0

                        for check in check_spots:
                            x = check[0]
                            y = check[1]

                            # out of bounds check
                            if (x < 0) or (y < 0) or (y >= len(line)) or (x >= len(grid)):
                                continue
                            if grid[x][y] == '@':
                                adj += 1
                           
                        if adj < 4:
                            grid[i][j] = '.' # replace box
                            to_add += 1
            accessible += to_add
    
    return accessible

if __name__ == '__main__':
    # tests and input filepaths
    test_fp = './tests/test_input.txt'
    input_fp = './tests/input.txt'

    assert part_1(test_fp) == 13
    assert part_2(test_fp) == 43

    # actual output
    print(part_1(input_fp))
    print(part_2(input_fp))
