with open("source/24.15.txt") as f:
    data = f.readline()

for a in range(1, 1000):
    if data.find("КОТ"*a) == -1:
        print(a-1)
        break

#ans: 75