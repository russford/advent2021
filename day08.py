import itertools


def read_data ():
    with open("day08.txt", "r") as f:
        return [a.split(' ') for l in f.readlines() for a in l.strip().split(" | ")]


def day1 (data):
    lens = [2, 3, 4, 7]
    s = 0
    for l in data[1::2]:
        s += sum (1 for a in l if len(a) in lens)
    print (s)


match = { "abcefg": 0,
          "cf": 1,
          "acdeg": 2,
          "acdfg": 3,
          "bcdf": 4,
          "abdfg": 5,
          "abdefg": 6,
          "acf": 7,
          "abcdefg": 8,
          "abcdfg": 9 }


def check (strings, key):
    translate = [''.join(sorted([key[ord(c)-ord("a")] for c in s])) for s in strings]
    return all (t in match for t in translate)


def decode (message, key):
    decoded = ''.join(sorted([key[ord(c)-ord("a")] for c in message]))
    return str(match[decoded])


def day2 (data):
    total = 0
    for i in range(len(data) // 2):
        values, message = data[2*i], data[2*i+1]
        for key in itertools.permutations("abcdefg"):
            if check (values, key):
                total += int(''.join([decode(m, key) for m in message]))
                break
    print (total)


if __name__ == "__main__":
    data = read_data()
    print(data)

    day1 (data)
    day2 (data)
