def f(nc, kc):
    if nc > kc:
        return 0
    if nc == kc:
        return 1
    if nc < kc:
        return f(nc+1, kc) + f(nc*4, kc)

print(f(10,100))

def f(nc, kc):
    if nc > kc:
        return 0
    if nc == kc:
        return 1
    if nc < kc:
        return f(nc+1, kc) + f(nc*3, kc) + f(nc*4, kc)

print(f(10,100))

def g(current):
    new = ""
    for symbol in str(current):
        newSymbol = str(int(symbol)+1)
        new = new + newSymbol
    return int(new)


def f(nc, kc):
    if nc > kc:
        return 0
    if nc == kc:
        return 1
    if nc < kc:
        return f(nc+1, kc) + f(g(nc), kc)

print(f(24,46)) #Ответ: 13

def g(current):
    new = ""
    for symbol in str(current):
        newSymbol = str(int(symbol)+1)
        new = new + newSymbol
    return int(new)


def f(nc, kc):
    if nc > kc:
        return 0
    if nc == kc:
        return 1
    if nc < kc:
        return f(nc+1, kc) + f(g(nc), kc)

print(f(26,49)) #Ответ: 16