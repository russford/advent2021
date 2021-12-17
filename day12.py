
def read_data ():
    with open("day12.txt", "r") as f:
        paths = [tuple(l.strip().split("-")) for l in f.readlines()]
    nodes = set([p for e in paths for p in e])
    data = {}
    for n in nodes:
        conns = [p for p in paths if n in p]
        data [n] = [ci for c in conns for ci in c if ci != n]
    return data


def day1 (data):
    paths = [["start"]]
    final = []
    while paths:
        path = paths.pop()
        if path[-1] == "end":
            final.append(path)
        else:
            for n in data[path[-1]]:
                if n not in path or n.isupper():
                    paths.append(path+[n])
    print (len(final))




def day2(data):
    paths = [(["start"], 0)]
    final = []
    while paths:
        path, double = paths.pop()
        if path[-1] == "end":
            final.append(path)
        else:
            for n in data[path[-1]]:
                # if n != "start" and (n not in path or no or n.isupper():
                #     paths.append(path+[n])
                if n.isupper() or n not in path:
                    paths.append((path+[n], double))
                elif n != "start" and not double:
                    paths.append((path+[n], 1))
    print (len(final))

if __name__ == "__main__":
    data = read_data()
    print(data)

    day1 (data)
    day2 (data)
