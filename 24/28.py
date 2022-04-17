with open("source/24.28.txt") as f:
    data = f.readline()

maxi = count = countA = 0

for a in range(len(data)):
    count += 1
    if data[a] == "A":
        countA += 1

    elif data[a] == "B":
        count -= 1
        if countA >= 3:
            maxi = max(maxi, count)
        count, countA = 0, 0


maxi = max(maxi, count)

print(maxi)