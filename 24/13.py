with open("source/24.13.txt") as f:
    data = f.readline()

count = 0

for a in range(len(data)-2):
    arr = [data[a], data[a + 1], data[a + 2]]
    if arr[0] in "BCD" and arr[1] in "BDE" and arr[1] != arr[0] and \
        arr[2] in "BCE" and arr[2] != arr[1]:
        count += 1

print(count)

#ans: 1280