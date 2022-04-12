with open("source/24.15.txt") as f:
    data = f.readline()


count, maxi = 0, 0

for a in range(len(data)):
    if (data[a] == "К" and count % 3 == 0) or (data[a] == "О" and count % 3 == 1) or (data[a] == "Т" and count % 3 == 2):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 0

print(maxi)