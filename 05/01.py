# NOT FINISHED



class Interval:
    def __init__(self, start, length):
        self.start, self.length = start, length

    def is_empty(self):
        return len(self.intervals) == 0
    
    def intersect(self, other):
        if other.a + other.length - 1 < self.start:
            self.start = 0
            self.length = 0
        elif other



def solve(path):
    with open(path, "r") as f:
        data = f.read().split("\n\n")
    seeds = [int(s) for s in data[0].split(':')[1].split(" ") if len(s) > 0]
    i = 0
    seed_ranges = []
    while i < len(seeds):
        seed_ranges.append((seeds[i], seeds[i+1]))
        i += 2
    print(seed_ranges)
    maps_list = [[[int(n) for n in r.split(" ")] for r in m.split(":")[1].strip().split("\n")] for m in data[1:]]
    #print(maps_list)
    final_pos = []
    for s in seeds:
        pos = s
        for maps in maps_list:
            for (dst_start, src_start, range_length) in maps:
                if pos >= src_start and pos - src_start < range_length:
                    pos = dst_start + pos - src_start
                    break
        final_pos.append(pos)
    #print(final_pos)
    #result = min(final_pos)
    #print(f"result={result}")




solve("example.txt")