def simple(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return  False
    return True

for cur in range(485617, 485617+50):
    arr = [1]
    for div in range(2, int(cur**0.5) + 1):
        if cur % div == 0:
            if simple(div): arr.append(div)
            if div**2 != cur and simple(cur//div): arr.append(cur//div)
    for a in range(10):
        res = []
        for x in arr:
            if x % 10 == a:
                res.append(x)
        print(a, res)
