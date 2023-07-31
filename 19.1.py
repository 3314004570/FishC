nums = []

while True:
    get_num = input('请录入一个整数（输入STOP结束）：')
    
    if get_num == 'STOP':
        break
    nums.append(int(get_num))
    
target = int(input('请输入目标整数：'))

n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print('[', i, ',', j, ']')
