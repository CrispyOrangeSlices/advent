import sys


def main():
    filename = sys.argv[1]
    print(filename)
    with open(filename) as f:
        content = f.readlines()
        gw = {}
        effect = {}

        for line in content:
            line = line.strip().split(":")
            print(line)
            game = line[0].split(" ")
            game = [g for g in game if g]
            game = int(game[1])
            effect[game] = 1

        for line in content:
            line = line.strip().split(":")
            print(line)
            game = line[0].split(" ")
            game = [g for g in game if g]
            game = int(game[1])
            plays = line[1].split("|")
            wins = plays[0].split(" ")
            play = plays[1].split(" ")
            wins = [int(w) for w in wins if w]
            play = [int(w) for w in play if w]

            gw[game] = 0

            play = set(play)
            wins = set(wins)
            score = play.intersection(wins)

            if len(score) > 0:
                ps = len(score) - 1
                gw[game] = pow(2, ps)
            if len(score) > 0:
                for i in range(1, len(score) + 1):
                    if game + i in effect:
                        print(game + i, effect[game])
                        effect[game + i] += 1 * effect[game]

            #            print(game)
            print(effect.values())
            #           print(wins)
            #           print(play)
            print("Score", len(score))
            print("-" * 20)
        print(sum(gw.values()))
        print(sum(effect.values()))


if __name__ == "__main__":
    main()
