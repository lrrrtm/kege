with open("source/24.9.txt") as f:
    data = f.readline()

maxi, count = 0, 0

for a in data:
    if a in "BCDF":
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0

maxi = max(maxi, count)
print(maxi)