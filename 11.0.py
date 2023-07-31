steps = 7
i = 1
FIND = False

while i < 100:
    if (((i % 2) == 1) and ((i % 3) == 2) and ((i % 5) == 4) and ((i % 6) == 5) and ((i % 7) == 0)):
        FIND = True
        break
    else:
        if i % 7 == 0:
            steps = steps + 7
    i = i + 1

if FIND == True:
    print('阶梯数是：', steps)
else:
    print('在程序限定的范围内找不到答案！')
