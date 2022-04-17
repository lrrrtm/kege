with open("source/24.29.txt") as f:
    data = f.readline()

maxi = count = countB = 0

for a in range(len(data)):
    count += 1
    if data[a] == "B":
        countB +=1
    if countB > 2:
        count -= 1
        maxi = max(maxi, count)
        count, countB = 0, 0
maxi = max(maxi, count)

print(maxi)