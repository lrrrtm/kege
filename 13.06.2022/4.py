for N in range(1, 2000):
    try:
        N = abs(N)
        new = bin(N)[2:]
        new1 = new
        new = new + new[1] + new[0]
        R = int(new, 2)
        if R > 90:
            print(new1, new, R)
            print(N)
            break
    except Exception:
        pass