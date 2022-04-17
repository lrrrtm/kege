f = open("source/24.5.txt", "r")
data = f.readline()

dict = {a:0 for a in "QAZWSXEDCRFVTGBYHNUJMIKOLP"}

for a in range(len(data) - 1):
    if data[a] == 'B':
        dict[data[a+1]] += 1

4-5maxi, chr = 0, ""
for a in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
    if dict[a] > maxi:
        maxi = dict[a]
        chr = a

print(maxi, chr)
