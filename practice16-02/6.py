S = 20
D = [0]*S
Q = 0

f = open("input1.txt", 'r')
N = int(f.readline())

for k in range(1, N+1):
    x = int(f.readline())
    if x < S:
        for i in range(1, S-x):
            Q += D[i]
        D[x] += 1
f.close()
print(Q)
