import sys

max_cubes = {"red": 12, "green": 13, "blue": 14}


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.readlines()
        numbers = list()
        valid_games = []
        for games in content:
            valid = True
            game = games.split(":")[0].split(" ")[1]
            rolls = games.split(":")[1]
            rolls = rolls.split(";")
            for roll in rolls:
                cubes = roll.strip().split(",")
                for cube in cubes:
                    cube = cube.split(" ")
                    cube = [c for c in cube if c]
                    if max_cubes[cube[1]] < int(cube[0]):
                        valid = False
            if valid:
                valid_games.append(int(game))
        print(sum(valid_games))


if __name__ == "__main__":
    main()
