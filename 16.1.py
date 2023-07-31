import random

counts = int(input('请输入抛硬币的次数:'))
i = 0
up = 0
down = 0

print("开始抛硬币实验：")
while i < counts:
    num = int(random.randint(1,2))

    if num % 2:
        up += 1
            
        if counts < 100:
            print('正面 ', end='')
    else:
        down += 1
        
        if counts < 100:
            print('反面 ', end='')

    i = i + 1

print('\n一共模拟了', counts, '次抛硬币，结果如下：')
print('正面：', up, '次\n反面：', down, '次')
