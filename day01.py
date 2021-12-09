with open ("day01.txt", "r") as f:
    data = [int(a) for a in f.readlines()]

print (sum([1 if data[i+1] > data[i] else 0 for i in range(len(data)-1)]))


print (sum([1 if data[i+3] > data[i] else 0 for i in range(len(data)-3)]))