with open("source/test1.txt") as f:
    data = f.readline()

countAll, count, start = 0, 0, False

for a in range(len(data) - 1):
    if data[a] == "E" and not start:
        start = True
        count += 1
    elif data[a] != "E" and data[a] != "F" and start:
        count += 1
    else:
        if data[a] == "E" and start:
            if count >= 12:
                countAll += 1
            count, start = 1, False

        elif data[a] == "F":
            if count >= 12:
                countAll += 1
            count, start = 0, False
print(countAll)