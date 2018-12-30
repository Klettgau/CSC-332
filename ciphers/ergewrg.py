import random

setty = list()
res = list()
for x in range(25):
    setty.append(x)
for y in range(26):
    tmp = random.randint(0, 25)
    x = False
    while (not x):
        if setty.__contains__(tmp):
            res.append(setty.pop(setty.index(tmp)))
            x = True

        tmp = random.randint(0, 25)
print(res)
