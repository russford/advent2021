def read_data ():
    with open("day07.txt", "r") as f:
        return [int(a) for a in f.read().split(",")]

def cost (data, x):
    return sum((abs(x-d)*(abs(x-d)+1))//2 for d in data)


def day1 (data):
    x1, x2 = min(data), max(data)
    while True:
        guess = (x2+x1) // 2
        c = cost(data, guess)
        c_p = cost(data, guess-1)
        c_n = cost(data, guess+1)
        if c < c_n and c < c_p:
            break
        else:
            if c_p < c:
                x2 = guess
            else:
                x1 = guess
    print(guess, cost(data, guess))


def day2(data):
    pass


if __name__ == "__main__":
    data = read_data()
    # data = [16,1,2,0,4,2,7,1,2,14]
    print(cost(data, 2))

    day1 (data)
    day2 (data)
