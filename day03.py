def read_data ():
    with open("day03.txt", "r") as f:
        return [int(a, 2) for a in f.readlines()]


def day1 (data, n):
    counts = [1 if sum(a >> i & 1 for a in data) > len(data) // 2 else 0 for i in range(n)]
    counts.reverse()
    print (counts)
    a = int(''.join(str(c) for c in counts), 2)
    b = int('1'*n, 2) - a
    print (a, b, a*b)


def day2(data, n):
    mcv = data.copy()
    lcv = data.copy()

    for i in range(n-1, -1, -1):
        bit = 1 if 2 * sum(a >> i & 1 for a in mcv) >= len(mcv) else 0
        mcv = [a for a in mcv if (a >> i & 1) == bit]
        if len(mcv) == 1:
            break

    for i in range(n-1, -1, -1):
        bit = 1 if 2 * sum(a >> i & 1 for a in lcv) < len(lcv) else 0
        lcv = [a for a in lcv if (a >> i & 1) == bit]
        if len(lcv) == 1:
            break

    print (mcv[0] * lcv[0])


if __name__ == "__main__":
    data = read_data()

    day1 (data, 12)
    day2 (data, 12)
