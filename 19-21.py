from functools import lru_cache

def moves(h):
    a,b = h
    return (a+1,b), (a, b+1), (a*3, b), (a, b*3)

@lru_cache(None)
def f(h):
    if sum(h) >= 49:
        return "END"
    elif any(f(x) == "END" for x in moves(h)):
        return "П1"
    elif all(f(x) == "П1" for x in moves(h)):
        return "В1"
    elif any(f(x) == "В1" for x in moves(h)):
        return "П2"
    elif all(f(x) == "П2" or f(x) == "П1" for x in moves(h)):
        return "В2"

for i in range(1, 100):
    h = 5, i
    print(i, f(h))