# coding=gbk

Odd  = []#����
Even = []#ż��

num = input('������һ�������б�:')
num_list = [int(x) for x in num]
print('����ǰ���б�:', num_list)

for i in range(len(num_list)):
    if num_list[i] % 2 == 1:
        Odd.append(num_list[i])
    else:
        Even.append(num_list[i])

print('�������б�:', sorted(Odd) + sorted(Even))