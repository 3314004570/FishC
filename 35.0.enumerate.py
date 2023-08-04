# coding=gbk

sequence = ['abc', '456', '^&*']
start = 5

for i in range(len(sequence)):
    print('(', sequence[i], ',' ,i + start, ')', end = '')