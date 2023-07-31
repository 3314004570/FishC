import random

counts = int(input('请输入抛硬币的次数:'))
i = 0
up = 0
up_times = 0
up_max = 0
down = 0
down_times = 0
down_max = 0
last_times_coin = 'empty'

print("开始抛硬币实验：")
while i < counts:
    num = int(random.randint(1,2))

    if num % 2:
        up += 1
        
        if last_times_coin == '正面':
            up_times += 1

        elif last_times_coin == '反面':
            if(down_max < down_times):
                down_max = down_times
            down_times = 1

        last_times_coin = '正面'
            
        if counts < 100:
            print('正面 ', end='')
    else:
        down += 1
        
        if last_times_coin == '反面':
            down_times += 1

        elif last_times_coin == '正面':
            if(up_max < up_times):
                up_max = up_times
            up_times = 1
            
        last_times_coin = '反面'
        
        if counts < 100:
            print('反面 ', end='')

    i = i + 1

print('\n一共模拟了', counts, '次抛硬币，结果如下：')
print('正面：', up, '次\n反面：', down, '次')
print('最多连续正面：', up_max, '次\n最多连续反面：', down_max, '次')
