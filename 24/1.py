with open("11.txt") as f:
    data = f.readline()


maxi = 0

count = 0
for a in range(len(data)-1):
    if data[a] != data[a+1]:
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0
maxi = max(maxi, count)


print(maxi)