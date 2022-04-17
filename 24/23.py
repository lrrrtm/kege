import string

with open("source/24.23.txt") as f:
    data = f.readlines()

minAstr, mini = "", 1000000000

for line in data:
    if line.count("A") < mini:
        mini = line.count("A")

for line in data:
    if line.count("A") == mini:
        minAstr = line
        break

dict = {a:0 for a in string.ascii_uppercase}

for a in range(len(line) - 1):
    dict[line[a]] += 1

print(dict)