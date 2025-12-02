def part_1(fp: str) -> int:
    file = ''
    with open(fp) as f:
        file = f.readlines()
    
    ranges = file[0].split(',')
    total = 0

    for ran in ranges:
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            if num_len % 2 == 1:
                continue
            
            if str_num[:num_len//2] == str_num[num_len//2:]:
                total += num

    return total

def part_2(fp: str) -> int:
    file = ''
    with open(fp) as f:
        file = f.readlines()
    
    ranges = file[0].split(',')
    total = 0

    for ran in ranges:
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            possible = []
            for i in range(1, num_len // 2 + 1):
                if num_len % i == 0:
                    possible.append(i)
            
            for size in possible:
                flag = True
                for i in range(0, num_len - size, size):
                    if str_num[i:i+size] == str_num[i+size:i+(2*size)]:
                        continue
                    else:
                        flag = False
                if flag:
                    total += num
                    break
            
    return total

def part_2_new(fp: str) -> int:
    ranges = ''
    total = 0

    with open(fp) as f:
        ranges = f.read().split(',')

    for ran in ranges:
        ran = ran.split('-')
        low = int(ran[0])
        high = int(ran[1])

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            for i in range(1, num_len // 2 + 1):
                if (num_len % i == 0) and ((str_num[:i] * (num_len//i)) == str_num):
                    total += num
                    break
            
    return total

if __name__ == '__main__':
    fp = './tests/input.txt'
    test_fp = './tests/test_input.txt'
    part_2_test = part_2(test_fp)

    assert part_2_test == 4174379265

    print(part_1(fp))
    print(part_2(fp))
    print(part_2_new(fp))