with open ("day02.txt", "r") as f:
    data = [l.strip('\n').split(" ") for l in f.readlines()]

x, y = 0, 0
aim = 0
for dir, amt in data:
    if dir == "forward":
        x += int(amt)
        y += aim * int(amt)
    elif dir == "down":
        aim += int(amt)
    else:
        aim -= int(amt)

print (x*y)