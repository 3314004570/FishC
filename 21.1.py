# coding=gbk

test = [2,2,4,2,3,6,2]

count = 0

i = 0

while i < len(test):
    if count == 0:
        Boss = test[i]
        count += 1

    else:
        if Boss == test[i]:
            count += 1
        else:
            count -= 1
    i += 1

if test.count(Boss) >= len(test) / 2:
    print('存在主要元素')

else:
    print('不存在主要元素')