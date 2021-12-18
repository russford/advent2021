import collections

def read_data ():
    with open("day14test.txt", "r") as f:
        data = f.read().split("\n\n")
        rules = collections.defaultdict(str)
        for line in data[1].split('\n'):
            c1, c2 = tuple(line.split(" -> "))
            rules[c1] = c2
        return data[0], rules

def iterate (s, rules, n):
    counter = collections.defaultdict(int)
    for c in s:
        counter[c] += 1
    for step in range(n):
        new = ""
        for i in range(len(s)-1):
            ins = rules[s[i:i+2]]
            if ins:
                counter[ins] += 1
            new += s[i] + ins
        s = new + s[-1]
        print (len(s))
    print (max(counter.values()) - min(counter.values()))

def count_pairs(s, rules, n):
    pairs = collections.defaultdict(int)
    for i in range(len(s)-1):
        pairs[s[i:i+2]] += 1
    print (pairs)
    for i in range(n):
        next = collections.defaultdict(int)
        for pair, count in pairs.items():
            if pair in rules:
                next[pair[0]+rules[pair]] += count
                next[rules[pair]+pair[1]] += count
        pairs = next

        char_count = collections.defaultdict(int)
        for pair, count in pairs.items():
            for p in pair:
                char_count[p] += count
        print (char_count)
        print ()





def day1 (start, rules):
    iterate(start, rules, 10)


def day2(start, rules):
    count_pairs(start, rules, 10)


if __name__ == "__main__":
    start, rules = read_data()

    day1 (start, rules)
    day2 (start, rules)
