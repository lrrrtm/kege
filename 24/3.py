f = open("24.3.txt", "r")
data = f.readlines()

count = 0
for a in data:
    if a.count("A") > a.count("B"):
        count+=1

print(count)
