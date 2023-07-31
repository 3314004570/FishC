"""用python设计第一个游戏"""

import random

times = 3
answer = random.randint(1, 10)

while times > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:")
    guess = int(temp)

    if guess == answer:
        print("你是小甲鱼心里的蛔虫嘛?!")
        print("哼,猜中了也没奖励!")
        break
    else:
        if guess < answer:
            print('小啦')
        else:
            print('大啦')
    times = times - 1

print("游戏结束,不玩啦^_^")
