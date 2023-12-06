import sys


def main():
    filename = sys.argv[1]
    print(filename)
    with open(filename) as f:
        content = f.readlines()
        times = None
        dists = None
        for line in content:
            if "Time" in line:
                line = line.strip()
                line = line.split(":")[1]
                line = line.split(" ")
                times = [int(t) for t in line if len(t) > 0]
            elif "Distance" in line:
                line = line.strip()
                line = line.split(":")[1]
                line = line.split(" ")
                dists = [int(d) for d in line if len(d) > 0]

        races = len(dists)

        ways = []

        dist = ""
        for d in dists:
            dist += str(d)

        timey = ""
        for t in times:
            timey += str(t)

        timey = int(timey)
        dist = int(dist)

        print(combs(timey, dist))


def combs(time, record):
    # Left
    start = 0
    speed = 0
    while start < time:
        speed = start
        if (time - start) * speed > record:
            break
        start += 1
    start_r = time
    while start_r > 0:
        speed = start_r

        if (time - start_r) * speed > record:
            break
        start_r -= 1

    return start_r - start + 1


if __name__ == "__main__":
    main()
