import collections

def read_data ():
    with open("day20.txt", "r") as f:
        alg, img_data = f.read().split("\n\n")

    img = set()
    for i, l in enumerate(img_data.split()):
        for j, c in enumerate(l):
            if c == "#": img.add((j,i))
    return alg, img

def bounds(img, push=0):
    return (min(a[0] for a in img)-push,
            max(a[0] for a in img)+push,
            min(a[1] for a in img)-push,
            max(a[1] for a in img)+push)

def print_img(img):
    x1, x2, y1, y2 = bounds(img)
    print ("\n".join(["".join(["#" if (x,y) in img else "." for x in range(x1, x2+1)]) for y in range(y1, y2+1)]))


def process_img (img, alg):
    check = [(-1, -1), (0, -1), (1, -1),
             (-1,  0), (0,  0), (1,  0),
             (-1,  1), (0,  1), (1,  1)]

    alg_func = lambda x, y: int("".join(["1" if (x+c[0], y+c[1]) in img else "0" for c in check]), 2)

    x1, x2, y1, y2 = bounds(img, 1)
    next_img = set()
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if alg[alg_func(x, y)] == "#": next_img.add((x, y))
    return next_img


def day1 (alg, img):
    for i in range(2):
        img = process_img(img, alg)
        print(len(img))
        print()




if __name__ == "__main__":
    alg, img = read_data()

    print_img(img)
    print()
    day1 (alg, img)
