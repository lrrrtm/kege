import string

with open("source/24.27.txt") as f:
    data = f.readlines()

minNstr, mini = "", 1000000000

for line in data:
    if line.count("N") < mini:
        mini = line.count("N")

for line in data:
    if line.count("N") == mini:
        minNstr = line
        break

dict = {a:0 for a in string.ascii_uppercase}

for a in range(len(line) - 1):
    dict[line[a]] += 1

print(dict)