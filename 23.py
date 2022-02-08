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
# def f(nc, kc, step):
#     if nc > kc or step > 4:
#         return 0
#     if nc == kc:
#         return 1
#     if nc < kc:
#         return f(nc*5, kc, step + 1) + f(nc//3, kc, step + 1)
#
# k, nc, step = 0, 81, 0
# for kc in range(81, 1000):
#     if f(nc, kc, step):
#         k += 1
# print(k)