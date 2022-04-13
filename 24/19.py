with open("source/24.19.txt") as f:
    data = f.readline()

count = 0

for a in range(2, len(data)-2):
    if data[a] == "O" and data[a + 1] == "C" and data[a + 2] == "K" and data[a - 1] != "T" and data[a - 2] != "S":
        count += 1

print(count)