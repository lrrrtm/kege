def g(current):
    if current == 9:
        return 9
    else:
        first = str(int(str(current)[0]) + 1)
        end = str(current)[1:]
        return int(first + end)


print(g(10))