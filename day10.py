def read_data ():
    with open("day10.txt", "r") as f:
        return [l.strip() for l in f.readlines()]


def process_1 (s):
    values = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    matched = {")":"(", "]": "[", "}": "{", ">": "<"}
    stack = ""
    for c in s:
        if c in matched.values():
            stack += c
        elif c in matched:
            if stack[-1] == matched[c]:
                stack = stack[:-1]
            elif c in values:
                return values[c]
    return 0


def process_2 (s):
    values = {"(": 1, "[": 2, "{": 3, "<": 4}
    matched = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = ""
    for c in s:
        if c in matched.values():
            stack += c
        elif c in matched:
            if stack[-1] == matched[c]:
                stack = stack[:-1]
            else:
                return 0
    score = 0
    for c in stack[::-1]:
        score = score * 5 + values[c]
    return score


def day1(data):
    print (sum(process_1(s) for s in data))


def day2(data):
    scores = [process_2(s) for s in data]
    scores = [s for s in scores if s > 0]
    print (sorted(scores)[len(scores)//2])


if __name__ == "__main__":
    data = read_data()
#     data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

    day1 (data)
    day2 (data)
