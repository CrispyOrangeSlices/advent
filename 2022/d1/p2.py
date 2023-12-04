import sys


def main():
    filename = sys.argv[1]
    print(filename)
    with open(filename) as f:
        content = f.readlines()
        elf_totals = []
        elf_totals.append(0)
        for line in content:
            line = line.strip()
            if line == "":
                elf_totals.append(0)
            else:
                elf_totals[-1] += int(line)

        se = sorted(enumerate(elf_totals), key=lambda i: i[1], reverse=True)
        top_three = 0
        for idx, amt in se[:3]:
            top_three += amt
        print(top_three)


if __name__ == "__main__":
    main()
