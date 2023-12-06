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
                map[mdx].append(((a,a+sz), (b, b+sz)))
            else:
                pass

        print(seedr)
        seedf = list()
        for start, count in seedr:
            seedf.append((start, start+count))
        
        print(seedf)
        for key in map:
            print(map[key])
     

def helper(seed_range, mappings):
    # This returns the lowest possible seed output given a seed and list of mappings
    checks = list()
    checks.append(seed_range[0]) # The first seed
    for mapp in mappings:
        # For every mapping, The
        # Lower bound
        pass

    # Lowest Seed Not in a mapping 
    # Lowest seed in a mapping
    # Lowest valid output mapping seed


def tl(seed, mapping):
    upper = mapping[0][1]
    lower = mapping[0][0]
    tl_lower = mapping[1][0]
    if seed < mapping[0][1] and seed >= mapping[0][0]:
        return seed - lower + tl_lower
    return - 1




if __name__ == "__main__":
    main()
