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
        if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
            result += id + 1
        print(id+1, cubes)
    print(f"result={result}")


solve("input.txt")