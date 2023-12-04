def product(l):
    if len(l) == 0:
        return 1
    else:
        return l[0] * product(l[1:])

def solve(path):
    with open(path, "r") as f:
        games = [l.split(":")[1].strip() for l in f.readlines()]
    data = []
    result = 0
    for (id, g) in enumerate(games):
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        subsets = g.split(";")
        for s in subsets:
            draws = s.split(",")
            for c in draws:
                n, color = c.strip().split(" ")
                cubes[color] = max(cubes[color], int(n))
        result += product(list(cubes.values()))
    print(f"result={result}")


solve("input.txt")