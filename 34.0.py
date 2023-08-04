# coding=gbk

Odd  = []#奇数
Even = []#偶数

num = input('请输入一个整数列表:')
num_list = [int(x) for x in num]
print('排序前的列表:', num_list)

for i in range(len(num_list)):
    if num_list[i] % 2 == 1:
        Odd.append(num_list[i])
    else:
        Even.append(num_list[i])

print('排序后的列表:', sorted(Odd) + sorted(Even))