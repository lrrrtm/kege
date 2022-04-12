with open("source/24.7.txt") as f:
    data = f.readline()

maxi, count = 0, 0

for a in range(len(data)):
    if data[a] in 'ABC':
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0
maxi = max(maxi, count)

print(maxi)