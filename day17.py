def hits(v, tx, ty):
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
        if v[1] < 0 and pos[1] < ty[0]:
            break

        pos = (pos[0] + v[0], pos[1] + v[1])
        dxv = 0 if v[0] == 0 else 1 if v[0] < 0 else -1
        v = (v[0] + dxv, v[1] - 1)

        if pos[1] > y_max:
            y_max = pos[1]

    return result, y_max


def quad (a, b, c):
    term = (b*b - 4*a*c)**0.5
    return (-b+term)/(2*a), (-b-term)/(2*a)


def search (tx, ty):
    vx_max = tx[1]
    vx_min = int(max(quad(0.5, 0.5, -tx[0])))+1
    vy_min = ty[0]
    vy_max = -(ty[0]-1)

    print(vx_min, vx_max, vy_min, vy_max)

    count = 0

    for vx in range(vx_min, vx_max+1):
        for vy in range(vy_min, vy_max+1):
            hit, y = hits((vx, vy), tx, ty)
            if hit:
                count += 1
    print(count)


def day1(target):
    search (target[0], target[1])


if __name__ == "__main__":
    target = ((20, 30), (-10, -5))
    target = ((277, 318), (-92, -53))
    day1 (target)
