with open("source/24.4.txt") as f:
    data = f.readline()

start = end = 0

for a in range(1, len(data) - 1):
    if ord(data[a]) > ord(data[a - 1]) and ord(data[a]) > ord(data[a + 1]):
        start = a
        break

data = data[::-1]
for a in range(1, len(data) - 1):
    if ord(data[a]) > ord(data[a - 1]) and ord(data[a]) > ord(data[a + 1]):
        end = len(data) - 1 - a
        x = a
        break

print(end-start)