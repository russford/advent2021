
def day2(data):
    pass


patterns = [(0,1), (5, 1), (10, 1), (15, 1), (20, 1),
            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]


def check(card, numbers):
    return any(all(card[p[0]+p[1]*i] in numbers for i in range(5)) for p in patterns)


def day1 (cards, numbers):
    for i in range(1, len(numbers)):
        for c in cards:
            if check(c, numbers[:i]):
                return sum([a for a in c if a not in numbers[:i]]) * numbers[i-1]


def day2 (cards, numbers):
    for i in range(len(numbers)-1, -1, -1):
        losers = [c for c in cards if not check(c, numbers[:i])]
        if len(losers) == 1:
            return sum([a for a in losers[0] if a not in numbers[:i+1]] * numbers[i])


if __name__ == "__main__":
    with open ("day04.txt", "r") as f:
        data = f.read().split("\n\n")

    numbers = [int(a) for a in data[0].split(",")]
    cards = [[int(a) for a in d.split()] for d in data[1:]]

    print(day1(cards, numbers))
    print(day2(cards, numbers))


