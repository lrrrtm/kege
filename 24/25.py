with open("source/24.25.txt") as f:
    data = f.readline()

maxi, count = 0, 0
fl = False

for a in range(len(data)):
    count += 1
    if data[a] == "A" and not fl:
        fl = True

    elif data[a] == "A" and fl:
        count -= 1
        maxi = max(maxi, count)
        count, fl = 1, False


maxi = max(maxi, count)

print(maxi)

#ans: 286