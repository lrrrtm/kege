S = 20
Q = 0
D = [0] * S
F = open("test.txt", "r")
N = int(F.readline())
for i in range(1, N+1):
    x = int(F.readline())
    if x >= S:
        for j in range(1, S - x + 1):
            Q += D[j]
        D[x] += 1
    if x < S:
        for k in range(S - x + 1, 20):
            Q += D[k]
        D[x] += 1
F.close()
print(Q)