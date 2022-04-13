with open("source/24.18.txt") as f:
    data = f.readline()

count = 0

for a in range(1, len(data)-3):
    if data[a - 1] != "J" and data[a:a+4] == "BOSS" and data[a + 4] != "J":
        count +=1
        #print(data[a-1:a+5])

print(count)