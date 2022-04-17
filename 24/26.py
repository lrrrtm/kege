import string

with open("source/24.26.txt") as f:
    data = f.readlines()



for line in data:
    if line.count("A") < 25:
        maxi = 0
        #print("OK")
        for symb in string.ascii_uppercase:
            start = line.find(symb)
            line = line[::-1]
            end = len(line) - 1 - line.find(symb)
            #print(symb, start, end)
            if end - start > maxi:
                maxi = end - start
        print(maxi)


