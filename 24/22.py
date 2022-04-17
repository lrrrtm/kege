with open("source/24.22 .txt") as f:
    data = f.readline()

count = maxi = 0

for a in range(len(data) - 1):
    if data[a] == data[a + 1]:
        count += 1
    else:
        if count > maxi:
            maxi = count
        count = 0

for a in range(len(data) - 1):
    if data[a] == data[a + 1]:
        count += 1
    else:
        if count == maxi:
            print(data[a], maxi)
            break
