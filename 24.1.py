# coding=gbk

i = 1
numlist = [1]

while i < 11:
    times = 0 + 3 * i
    while times < 30:
        print(' ', end = '')
        times += 1

    times = 0
    j = 1
    if i > 2:
        while j < i - 1:
            numlist.insert(j, lastlist[j - 1] + lastlist[j])
            j += 1

    #打印存储的数字
    while times < len(numlist):
        if numlist[times] < 10:
            print(numlist[times], '    ', end = '')
        elif numlist[times] < 100:
            print(numlist[times], '   ', end = '')
        else:
            print(numlist[times], '  ', end = '')
        times += 1
    print('')

    #向存储的数字末尾加1
    if i == 1:
        numlist.append(1)
    else:
        lastlist = numlist
        numlist = [1,1]
    i += 1