with open("source/test.txt") as f:
    data = f.readline()

maxi, count = 0, 0

for a in data:
    if a in "ABCEF":
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0
maxi = max(maxi, count)

print(maxi)
