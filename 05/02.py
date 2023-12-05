def solve(path):
    with open(path, "r") as f:
        data = f.read().split("\n\n")
    seeds = [int(s) for s in data[0].split(':')[1].split(" ") if len(s) > 0]
    print(seeds)
    maps_list = [[[int(n) for n in r.split(" ")] for r in m.split(":")[1].strip().split("\n")] for m in data[1:]]
    print(maps_list)
    final_pos = []
    for s in seeds:
        pos = s
        for maps in maps_list:
            for (dst_start, src_start, range_length) in maps:
                if pos >= src_start and pos - src_start < range_length:
                    pos = dst_start + pos - src_start
                    break
        final_pos.append(pos)
    print(final_pos)
    result = min(final_pos)
    print(f"result={result}")




solve("input.txt")