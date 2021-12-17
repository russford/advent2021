import re

def read_data ():
    with open("day13.txt", "r") as f:
        data = f.read()
        dots = [(int(a), int(b)) for a, b in re.findall("(\d+),(\d+)", data)]
        lines = [(a, int(b)) for a, b in re.findall("(x|y)=(\d+)", data)]
    return dots, lines

def fold_points (points, axis, fold):
    pos_side = [p for p in points if p[axis] > fold]
    if axis == 0:
        points = [(p[0] if p[0] < fold else 2 * fold - p[0], p[1]) for p in points]
    else:
        points = [(p[0], p[1] if p[1] < fold else 2 * fold - p[1]) for p in points]
    return list(set(points))


def day1 (data):
    points, folds = data
    for axis, fold in folds:
        points = fold_points(points, 0 if axis == "x" else 1, fold)
        print (len(points))

    x_min = min(p[0] for p in points)
    x_max = max(p[0] for p in points)
    y_min = min(p[1] for p in points)
    y_max = max(p[1] for p in points)

    for j in range(y_min, y_max+1, 1):
        print (''.join(["#" if (i, j) in points else "." for i in range(x_min, x_max+1, 1)]))

def day2(data):
    pass


if __name__ == "__main__":
    data = read_data()
    print(data)

    day1 (data)
    day2 (data)
