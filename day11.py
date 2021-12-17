def read_data ():
    data = """8548335644
6576521782
1223677762
1284713113
6125654778
6435726842
5664175556
1445736556
2248473568
6451473526"""
#     data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""
#     data = """11111
# 19991
# 19191
# 19991
# 11111"""
    return [[int(a) for a in l] for l in data.split("\n")]

def iterate (data):
    check = []
    flashed = []
    x_max = len(data[0])
    y_max = len(data)
    for x in range(x_max):
        for y in range(y_max):
            data[y][x] += 1
            if data[y][x] > 9:
                check.append((x, y))
                flashed.append((x, y))
    while True:
        next = []
        while check:
            x, y = check.pop()
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x+dx < x_max and 0 <= y+dy < y_max and (dx != 0 or dy != 0):
                        data[y+dy][x+dx] += 1
                        if data[y+dy][x+dx] > 9 and (x+dx, y+dy) not in flashed:
                            flashed.append((x+dx, y+dy))
                            next.append((x+dx, y+dy))
        if next:
            check = next
        else:
            break
    for x, y in flashed:
        data[y][x] = 0
    return len(flashed)


def day1 (data, n):
    flashed = 0
    for i in range(n):
        flashed += iterate(data)
    print (flashed)


def day2(data):
    i = 0
    while True:
        i += 1
        if iterate(data) == len(data)*len(data[0]):
            print (100+i)
            break



if __name__ == "__main__":
    data = read_data()

    day1 (data, 100)
    day2 (data)
