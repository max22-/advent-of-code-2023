def solve(path):
    with open(path, "r") as f:
        cards = f.readlines()
    cards = [card.split(":")[1].strip() for card in cards]
    result = 0
    for c in cards:
        winning_numbers = [int(n) for n in c.split("|")[0].split(" ") if len(n) > 0]
        numbers_i_have = [int(n) for n in c.split("|")[1].split(" ") if len(n) > 0]
        print(f"{winning_numbers} {numbers_i_have}")
        matches = len(set(winning_numbers).intersection(set(numbers_i_have)))
        points = 2 ** (matches - 1) if matches > 0 else 0
        print(f"points: {points}")
        result += points
    print(f"result: {result}")

solve("input.txt")