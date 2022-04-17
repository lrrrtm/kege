with open("source/24.4.txt") as f:
    data = f.readline()

start = end = 0
maxi = 0

for a in range(1, len(data) - 1):
    if ord(data[a]) > ord(data[a - 1]) and ord(data[a]) > ord(data[a + 1]):
        start, end = end, a
        maxi = max(maxi, (end - start))



print(maxi)