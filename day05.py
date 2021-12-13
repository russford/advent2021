import re
import collections

def read_data ():
    with open("day05.txt", "r") as f:
        return [int(a) for a in re.findall("\d+", f.read())]


def day1(data):
    points = collections.defaultdict(int)
    while data:
        line, data = data[:4], data[4:]
        if line[0] == line[2]:
            y1, y2 = line[1], line[3]
            if y2 < y1:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                points[(line[0], i)] += 1
        if line[1] == line[3]:
            x1, x2 = line[0], line[2]
            if x2 < x1:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                points[(i, line[1])] += 1

    print (sum([1 for v in points.values() if v > 1]))

def day2(data):
    points = collections.defaultdict(int)
    while data:
        line, data = data[:4], data[4:]
        x1, y1, x2, y2 = tuple(line)
        x_step = 0 if x1 == x2 else (-1 if x2 < x1 else 1)
        y_step = 0 if y1 == y2 else (-1 if y2 < y1 else 1)
        for i in range(max(abs(y2-y1), abs(x2-x1))+1):
            points[(x1+i*x_step, y1+i*y_step)] += 1

    print(sum([1 for v in points.values() if v > 1]))


if __name__ == "__main__":
    data = read_data()

    day1 (data)
    day2 (data)
