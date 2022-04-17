with open("source/24.3.txt") as f:
    data = f.readline()

count = 0

for a in data:
    if a.count("A") > a.count("B"):
        count += 1

print(count)
