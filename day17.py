


def hits (v, tx, ty):
    pos = (0, 0)
    y_max = 0
    result = False
    while True:
        if tx[0] <= pos[0] <= tx[1] and ty[0] <= pos[1] <= ty[1]:
            result = True
            break
        if v[0] == 0 and (pos[0] < tx[0] or pos[0] > tx[1]):
            break
        if v[0] < 0 and pos[0] < tx[0]:
            break
        if v[0] > 0 and pos[0] > tx[1]:
            break
        if v[1] < 0 and pos[1] < ty[1]:
            break

        pos = (pos[0] + v[0], pos[1] + v[1])
        dxv = 0 if v[0] == 0 else 1 if v[0] < 0 else -1
        v = (v[0] + dxv, v[1] - 1)

        if pos[1] > y_max:
            y_max = pos[1]

    if result:
        print (y_max)

    return result

def quad (a, b, c):
    term = (b*b - 4*a*c)**0.5
    return ((-b + term)/(2*a))


def search (tx, ty):
    vx_max = tx[1]
    vx_min = ((-1 + (1 + 4 * tx[0]) ** 0.5) // 2)

    t_min = 1
    t_max = vx_min + 1



def day1(target):
    for p in [(7,2), (6, 3), (9, 0), (17, -4), (6, 9)]:
        print (p, hits(p, *target))


def day2(data):
    pass


if __name__ == "__main__":
    target = ((20, 30), (-10, -5))
    day1 (target)
    day2 (target)
