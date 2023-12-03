import sys

max_cubes = {"red": 12, "green": 13, "blue": 14}


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.readlines()


if __name__ == "__main__":
    main()
