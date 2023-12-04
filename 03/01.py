def print_matrix(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            print(m[y][x], end="")
        print("")
    print("")

def solve(path):
    with open(path, "r") as f:
        schematic = [l.strip() for l in f.readlines()]
    print(schematic)
    w = len(schematic[0])
    h = len(schematic)
    def inside(x, y):
        return x >= 0 and y >= 0 and x < w and y < h
    def neighbours(x, y):
        ns = [(x+i, y+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
        return [(i, j) for (i, j) in ns if inside(i, j)]
    def isdigit(x, y):
        return schematic[y][x] >= '0' and schematic[y][x] <= '9'
    
    neighbours_mask = [[0 for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if not(isdigit(x, y)) and schematic[y][x] != '.':
                for (i, j) in neighbours(x, y):
                    neighbours_mask[j][i] = 1
    print_matrix(neighbours_mask)
    keep_mask = [[0 for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if isdigit(x, y) and neighbours_mask[y][x] == 1:
                i = x
                while i >= 0 and isdigit(i, y):
                    keep_mask[y][i] = 1
                    i -= 1
                i = x
                while i < w and isdigit(i, y):
                    keep_mask[y][i] = 1
                    i += 1
    print_matrix(keep_mask)

    filtered_schematic = [[schematic[y][x] if keep_mask[y][x] else '.' for x in range(w)] for y in range(h)]
    
    filtered_schematic = [[e for e in ''.join(l).split('.') if len(e) > 0] for l in filtered_schematic]

    nums = [int(e) for line in filtered_schematic for e in line]
    

    print(filtered_schematic)
    print(nums)
    print(f"solution: ", sum(nums))


solve("input.txt")