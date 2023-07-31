import random
nums = []

for i in range(10000):
    nums.append(random.randint(1,65535))
    
target = int(input('请输入目标整数：'))

n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print('[', i, ',', j, ']')
