with open("source/24.6.txt") as f:
    data = f.readline()

index = count = 0

for a in range(len(data) - 1):
    if count != 10000:
        if data[a] == "(" and data[a + 1] == ")":
            index = a
            count += 1
    else:
        print(index)
        break
