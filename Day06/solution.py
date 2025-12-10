import re

def part_1(fp: str) -> int:
    with open(fp) as f:
        first_line = f.readline().strip()
        sums = [int(num.strip()) for num in re.split(r'\s+', first_line)]
        products = [int(num.strip()) for num in re.split(r'\s+', first_line)]
        total = 0

        for line in f:
            line_split = re.split(r'\s+', line.strip())
            
            for i, num in enumerate(line_split):
                if num == '*':
                    total += products[i]
                elif num == '+':
                    total += sums[i]
                else:
                    num = int(num.strip())
                    sums[i] += num
                    products[i] *= num
        return total

def part_2(fp: str) -> int:
    with open(fp) as f:

        return 0

if __name__ == '__main__':
    test_fp = './tests/test_input.txt'
    input_fp = './tests/input.txt'

    assert part_1(test_fp) == 4277556
    assert part_2(test_fp) == 3263827

    print(part_1(input_fp))