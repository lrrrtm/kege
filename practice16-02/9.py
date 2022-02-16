file = open("input9.txt", "r")
array = []
for x in file:
    array.append(int(x))

n = array[0]
array.pop(0)

count = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if (array[i] - array[j]) % 60 == 0 and array[i] > 80:
                count += 1

print(count//2)
