import random

counts = int(input('请输入抛硬币的次数:'))
i = 0

print("开始抛硬币实验：")
while i < counts:
    num = int(random.randint(1,2))

    if num % 2:
        print('正面')
    else:
        print('反面')

    i = i + 1
