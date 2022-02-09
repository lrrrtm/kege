#дополнительные вычисления
def g(current):
    if current == 9:
        return 9
    else:
        first = str(int(str(current)[0]) + 1)
        end = str(current)[1:]
        return int(first + end)

#без количества
def f(nc, kc):
    if nc > kc:
        return 0
    if nc == kc:
        return 1
    if nc < kc:
        return f(nc+1, kc) + f(g(nc), kc)

print(f(10,33))

#количество чисел
lst = set()
def f(n,k):
    if k == 5:
        lst.add(n)
        return 0
    f(n+4, k +1)
    f(n*2, k + 1)

f(2,0)
print(lst)
print(len(lst))
