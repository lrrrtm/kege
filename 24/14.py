with open("source/24.14.txt") as f:
    data = f.readline()

count = 0

for a in range(len(data)-4):
    arr = [data[a], data[a + 1], data[a + 2], data[a + 3], data[a + 4]]
    fl = True
    for i in range(len(arr)-1):
        if arr[i] == arr[i + 1]:
            fl = False
            break
    if fl:
        count +=1

print(count)