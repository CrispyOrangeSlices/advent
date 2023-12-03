import sys, re

symbols = {}


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.readlines()
        content = [c.strip() for c in content]
        valid_nums = []
        invalid_nums = []
        for ldx, line in enumerate(content):
            #    line = re.escape(line)
            num = ""
            is_part = False
            for cdx, c in enumerate(line):
                if c.isdigit():
                    num += c
                    if cdx == len(line) - 1:
                        determine_number(num, cdx, ldx, valid_nums, content)
                else:
                    if num != "":
                        determine_number(num, cdx, ldx, valid_nums, content)
                    num = ""
        print(sum(valid_nums))
        sum_gears = 0
        for s in symbols:
            if len(symbols[s]) == 2:
                sum_gears += symbols[s][0] * symbols[s][1]
        print(sum_gears)


def determine_number(num, cdx, ldx, valid_nums, content):
    is_part = False
    for ndx, n in enumerate(num):
        adx = cdx - (len(num) - ndx)
        status, symbol_pos = enumerate_position(ldx, adx, content)
        if status:
            is_part = True
            if symbol_pos in symbols:
                symbols[symbol_pos].append(int(num))
            else:
                symbols[symbol_pos] = [int(num)]
            break
    if is_part:
        valid_nums.append(int(num))
        num = ""
        is_part = False

    return valid_nums


def enumerate_position(x, y, content):
    ops = {-1, 0, 1}
    for i in ops:
        for j in ops:
            if check_position(x + i, y + j, content):
                return True, (x + i, y + j)
    return False, "Error"


def check_position(x, y, content):
    if x in range(0, len(content)):
        if y in range(0, len(content[x])):
            if content[x][y] in {"&", "%", "-", "@", "+", "=", "$", "/", "#", "*"}:
                return True
            else:
                return False


if __name__ == "__main__":
    main()
