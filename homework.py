def isSimple(n): #проверка числа на простоту
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return  False
    return True

for cur in range(485617, 529678+1):
    arr = [1] #список простых делителей числа, 1 у всех изначально
    for div in range(2, int(cur**0.5) + 1): 
        if cur % div == 0:
            if isSimple(div): arr.append(div) #если делитель простой, добавляем в список
            if div**2 != cur and isSimple(cur//div): arr.append(cur//div) #если старший делитель так же простой и не даёт само число при ^2, добавляем в список
    for lastNum in range(10): #проходимся по всем вариантам последней цифры числа (0..9)
        res = [] #список множителей числа
        for current in arr:
            if current % 10 == lastNum: #если у делителя числа нужная в данный момент последняя цифра, добавляем в список
                res.append(current)
        if len(res) == 3: #если в списке три элемента, проверяем, равно ли их произведение исходному числу
            q = 1
            for s in res:
                q *= s
            if q == cur and (max(res) - min(res)) < 100: #если произведение равно исходному числу и разница между максимальным и минимальным делителем < 100
                print(cur, res) #выводим это число + его множители
