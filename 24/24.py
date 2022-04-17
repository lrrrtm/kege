with open("source/24.24.txt") as f:
    data = f.readline()

maxi, count = 0, 0

for a in range(len(data)-1):
    if data[a] in "PQRS" and data[a] + data[a+1] != "PP":
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0
maxi = max(maxi, count)

print(maxi + 1)

#ans: 188