import sys


letters = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.readlines()
        numbers = list()
        total = 0
        for line in content:
            num = ""
            for i, letter in enumerate(line):
                if letter.isdigit():
                    num += letter
                else:
                    if line[i : i + 3] == "one":
                        print(line[i : i + 3])
                        num += "1"
                    elif line[i : i + 3] == "two":
                        num += "2"
                    elif line[i : i + 5] == "three":
                        num += "3"
                    elif line[i : i + 4] == "four":
                        num += "4"
                    elif line[i : i + 4] == "five":
                        num += "5"
                    elif line[i : i + 3] == "six":
                        num += "6"
                    elif line[i : i + 5] == "seven":
                        num += "7"
                    elif line[i : i + 5] == "eight":
                        num += "8"
                    elif line[i : i + 4] == "nine":
                        num += "9"

            print(num)
            numbers.append(int("" + num[0] + num[-1]))
        print(numbers)
        total = sum(numbers)
        print(sum(numbers))


if __name__ == "__main__":
    main()
