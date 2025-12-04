def part_1(fp:str) -> int:
    with open(fp) as f:
        grid = f.readlines()
        accessible = 0

        for i, line in enumerate(grid):
            line = line.strip()
            for j, spot in enumerate(line):
                if spot == '@':
                    check_spots = [(i-1, j), (i+1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
                    adj = 0
                    for check in check_spots:
                        if (check[0] < 0) or (check[1] < 0) or (check[1] >= len(line)) or (check[0] >= len(grid)):
                           continue
                        if grid[check[0]][check[1]] == '@':
                            adj += 1
                    if adj < 4:
                        accessible += 1
    
    return accessible

def part_2(fp:str) -> int:
    with open(fp) as f:
        grid = f.readlines()
        grid = [list(line.strip()) for line in grid]
        accessible = 0
        to_add = -1

        while to_add != 0:
            to_add = 0

            for i, line in enumerate(grid):
                for j, spot in enumerate(line):
                    if spot == '@':
                        check_spots = [(i-1, j), (i+1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
                        adj = 0
                        for check in check_spots:
                            if (check[0] < 0) or (check[1] < 0) or (check[1] >= len(line)) or (check[0] >= len(grid)):
                                continue
                            if grid[check[0]][check[1]] == '@':
                                adj += 1
                        if adj < 4:
                            grid[i][j] = '.'
                            to_add += 1
            accessible += to_add
    
    return accessible

if __name__ == '__main__':
    test_fp = './tests/test_input.txt'
    input_fp = './tests/input.txt'

    assert part_1(test_fp) == 13
    assert part_2(test_fp) == 43

    print(part_1(input_fp))
    print(part_2(input_fp))
