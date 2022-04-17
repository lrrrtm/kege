with open("source/24.2.txt") as f:
    data = f.readline()

maxi = count = 0, 1

for a in range(len(data)-1):
    if data[a] == data[a+1]:
        count +=1
    else:
        maxi = max(maxi, count)
        count = 1
maxi = max(maxi, count)

print(maxi)
