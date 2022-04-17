with open("source/24.11.txt") as f:
    data = f.readlines()

str, countG = "", 10**10

for a in data:
    if a.count("G") < countG:
        countG = a.count("G")
        str = a

for a in data:
    if a.count("G") == countG:
        str = a[:-1]
        break

dict = {a: 0 for a in "QWERTYUIOPASDFGHJKLZXCVBNM"}

for a in range(len(str)):
    dict[str[a]] += 1

maxi = 0
for a in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
    maxi = max(maxi, dict[a])

print(maxi)
print(dict)

#ans: T