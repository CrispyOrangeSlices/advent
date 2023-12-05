import sys


def main():
    filename = sys.argv[1]
    print(filename)
    with open(filename) as f:
        content = f.readlines()
        map = {}
        mdx = -1
        seeds = None
        seedr = list()
        for line in content:
            if "seeds" in line:
                line = line.strip().split(":")
                seeds = line[1].split(" ")
                seeds = [s for s in seeds if s]
                seeds = [int(s) for s in seeds]
                print(seeds)
                sidx = 0
                while sidx < len(seeds):
                    seedr.append((seeds[sidx], seeds[sidx+1]))
                    sidx+=2
                print(seedr)
                                
            elif "map" in line:
                mdx += 1
                map[mdx] = list()
            #                print(mdx, line)
            ## Increment the map each time
            elif len(line) > 1:
                line = line.strip().split(" ")
                line = [int(i) for i in line]
                b = line[0]
                a = line[1]
                sz = line[2]
                map[mdx].append((a, b, sz))
            else:
                pass



        ## Instead, start at the last map and work our way up
        rmap = list(map.keys())
        rmap = list(reversed(rmap))
        print(rmap)
        print(map[rmap[0]])

        translations = dict()
        translations[0] = list()

        print("-" * 20)
        print(seeds)
        seedy = dict()
        for sdx, seed in enumerate(seeds):
            seedy[sdx] = [seed]
        print(map[0])
        for sey in seedy:
            for key in map:
                cseed = seedy[sey][-1]
                for t1 in map[key]:
                    res = helper(t1, cseed)
                    if res != -1:
                        cseed = res
                        break
                seedy[sey].append(cseed)
        locs = []
        for key in seedy:
            locs.append(seedy[key][-1])
            print(seedy[key])
        locs = sorted(locs)
        print("Answer", locs[0])


def helper(t1, seed):
    upper = t1[0] + t1[2]
    lower = t1[0]

    if seed >= lower and seed < upper:
        print("Success")
        return seed - lower + t1[1]
    print("Failure")
    return -1


if __name__ == "__main__":
    main()
