with open("source/24.10.txt") as f:
    data = f.readline()

dict = {a: 0 for a in "QWERTYUIOPASDFGHJKLZXCVBNM"}

for a in range(1, len(data) - 1):
    if data[a-1] == data[a+1]:
        dict[data[a]] += 1

maxi, chr = 0, ""

for a in "QWERTYUIOPASDFGHJKLZXCVBNM":
    if dict[a] > maxi:
        maxi = dict[a]
        chr = a

print(chr, maxi)

#ans: D