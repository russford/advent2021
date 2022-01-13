import re

class Snailfish (object):
    def __init__(self, s):
        self.s = [a if a in "[]" else int(a) for a in re.findall("(\[|\]|\d)", s)]

    def __str__(self):
        return ' '.join(str(c) for c in self.s)

    def reduce(self):
        while True:
            if not self.explode():
                if not self.split():
                    break

    def explode(self):
        bracket = 0
        for i, c in enumerate(self.s):
            bracket += (1 if c == "[" else 0) + (-1 if c == "]" else 0)
            if bracket == 5:
                break

        if c != "[":
            return 0

        for j in range(i-1, -1, -1):
            if self.s[j] != "[" and self.s[j] != "]":
                break
        if j > 0:
            self.s[j] += self.s[i+1]

        for j in range(i+3, len(self.s)):
            if self.s[j] != "[" and self.s[j] != "]":
                break
        if j < len(self.s)-1:
            self.s[j] += self.s[i+2]

        self.s = self.s[:i]+[0]+self.s[i+4:]
        return 1

    def split(self):
        for i, c in enumerate(self.s):
            if c != "[" and c != "]" and c > 9:
                break
        if c == "[" or c == "]":
            return 0

        self.s = self.s[:i] + ["[", c // 2, c // 2 + (1 if c % 2 else 0), "]"] + self.s[i+1:]
        return 1

    def add(self, n):
        self.s = ["["] + self.s + n.s + ["]"]
        self.reduce()

    def magnitude (self):
        m = self.s.copy()
        isb = lambda i: m[i]=="[" or m[i]=="]"
        while len(m) > 3:
            for i in range(len(m)-3):
                if isb(i) and not isb(i+1) and not isb(i+2) and isb(i+3):
                    m = m[:i] + [3 * m[i+1] + 2 * m[i+2]] + m[i+4:]
                    break
        return m[0]


def read_data ():
    with open("day18.txt", "r") as f:
        return f.read().split("\n")

def day1 (input):
    n = Snailfish(input[0])
    for l in input[1:]:
        n.add(Snailfish(l))
    print(n.magnitude())


def day2(input):
    n_max = 0
    for l1 in input:
        for l2 in input:
            if l1 != l2:
                n = Snailfish("["+l1+","+l2+"]")
                n.reduce()
                n_max = max(n_max, n.magnitude())
    print(n_max)


if __name__ == "__main__":
    input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")
    input = read_data()

    day1(input)
    day2(input)