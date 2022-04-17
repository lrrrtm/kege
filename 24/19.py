with open("source/24.19.txt") as f:
    data = f.readline()

count = 0


for a in range(len(data) - 4):
    line = data[a] + data[a + 1] + data[a + 2] + data[a + 3] + data[a + 4]
    if line[0] != "S" and line[1] != "T" and line[2:] == "OCK":
        count +=1

print(count)