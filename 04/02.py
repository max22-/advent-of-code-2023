def solve(path):
    with open(path, "r") as f:
        cards = f.readlines()
    cards = [card.split(":")[1].strip() for card in cards]
    scores = []
    matches_list = []
    for c in cards:
        winning_numbers = [int(n) for n in c.split("|")[0].split(" ") if len(n) > 0]
        numbers_i_have = [int(n) for n in c.split("|")[1].split(" ") if len(n) > 0]
        print(f"{winning_numbers} {numbers_i_have}")
        matches = len(set(winning_numbers).intersection(set(numbers_i_have)))
        matches_list.append(matches)
        points = 2 ** (matches - 1) if matches > 0 else 0
        scores.append(points)
        
    print(f"scores: {scores}")
    print(f"matches_list: {matches_list}")
    copies = [0 for i in range(len(cards))]
    stack = list(range(len(cards)))
    while len(stack) > 0:
        card = stack.pop()
        copies[card] += 1
        for i in range(matches_list[card]):
            stack.append(card + i + 1)
    print(f"copies={copies}")
    print(f"result={sum(copies)}")



solve("input.txt")