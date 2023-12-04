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
        midx = max(enumerate(elf_totals), key=lambda x: x[1])[0]
        mval = elf_totals[midx]
        print("Elf ", midx + 1, " has score: ", mval)


if __name__ == "__main__":
    main()
