import sys

max_cubes = {"red": 12, "green": 13, "blue": 14}


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.readlines()
        numbers = list()
        valid_games = []
        power_sets = []
        for games in content:
            min_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            valid = True
            game = games.split(":")[0].split(" ")[1]
            rolls = games.split(":")[1]
            rolls = rolls.split(";")
            for roll in rolls:
                cubes = roll.strip().split(",")
                for cube in cubes:
                    cube = cube.split(" ")
                    cube = [c for c in cube if c]
                    min_cubes[cube[1]] = max(min_cubes[cube[1]], int(cube[0]))
            ps = 1
            print(min_cubes)
            for key in min_cubes:
                ps *= min_cubes[key]
            power_sets.append(ps)

        print(sum(power_sets))


if __name__ == "__main__":
    main()
