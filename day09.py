def read_data ():
    with open("day09.txt", "r") as f:
        return [[int(a) for a in l.strip()] for l in f.readlines()]

def is_low (data, x, y):
    if x > 0 and data[y][x-1] <= data[y][x]: return False
    if x < len(data[0])-1 and data[y][x+1] <= data[y][x]: return False
    if y > 0 and data[y-1][x] <= data[y][x]: return False
    if y < len(data)-1 and data[y+1][x] <= data[y][x]: return False
    return True

def day1 (data):
    total = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if is_low(data, x, y):
                total += 1 + data[y][x]
    print(total)

def get_basin (data, x, y):
    check = [(x,y)]
    basin = []
    while check:
        x, y = check.pop()
        if data[y][x] < 9:
            basin.append((x,y))
            if x > 0 and data[y][x-1] < 9 and (x-1, y) not in basin and (x-1, y) not in check:
                check.append((x-1, y))
            if x < len(data[0])-1 and data[y][x+1] < 9 and (x+1, y) not in basin and (x+1, y) not in check:
                check.append((x+1, y))
            if y > 0 and data[y-1][x] < 9 and (x, y-1) not in basin and (x, y-1) not in check:
                check.append((x, y-1))
            if y < len(data)-1 and data[y+1][x] < 9 and (x, y+1) not in basin and (x, y+1) not in check:
                check.append((x, y+1))
    return basin



def day2(data):
    checked = []
    basins = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) not in checked:
                basin = get_basin(data, x, y)
                if basin:
                    basins.append(basin)
                    checked += basin
                else:
                    checked += (x, y)
    basins.sort(key=lambda b: -len(b))
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))



if __name__ == "__main__":
    data = read_data()

    day1 (data)
    day2 (data)
