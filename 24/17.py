with open("source/24.17.txt") as f:
    data = f.readline()


count = maxi = 0

for a in range(len(data)-2):
    if (data[a] == "T" and data[a + 1] == "I" and data[a + 2] == "K") or (data[a] == "T" and data[a + 1] == "O" and data[a + 2] == "K"):
        count += 1

print(count)