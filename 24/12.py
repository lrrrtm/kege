with open("source/24.12.txt") as f:
    data = f.readline()


count = maxi = 0

for a in range(len(data)):
    if (data[a] == "D" and count % 3 == 0) or (data[a] == "A" and count % 3 == 1) or (data[a] == "F" and count % 3 == 2):
        count += 1
        maxi = max(maxi, count)
    elif data[a] == "X":
        count = 1
    else:
        count = 0

print(maxi)