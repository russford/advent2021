import collections

def read_data ():
    with open("day06.txt", "r") as f:
        return [int(a) for a in f.read().split(",")]


def day1 (data):
    # for day in range(257):
    #     print (day, len(data))
    #     newfish = 0
    #     for i, fish in enumerate(data):
    #         if fish == 0:
    #             newfish += 1
    #             data[i] = 6
    #         else:
    #             data[i] -= 1
    #     data += [8]*newfish
    fish = collections.defaultdict(int)
    for d in data:
        fish[d] += 1
    for day in range(256):
        print
        newfish = fish[0]
        for i in range(8):
            fish[i] = fish[i+1]
        fish[6] += newfish
        fish[8] = newfish
    print (sum(fish.values()))




if __name__ == "__main__":
    data = [3, 4, 3, 1, 2]
    data = read_data()

    day1 (data)
