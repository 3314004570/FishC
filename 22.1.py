# coding=gbk

test = [2,3,2,4,2,3,6,2,3,3]

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

if test.count(Boss) >= len(test) / 3:
    print('占比最多的元素是', Boss)

i = 0
times = test.count(Boss)

while i < times:
    test.remove(Boss)
    i += 1

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

if test.count(Boss) >= len(test) / 3:
    print('占比第二多的元素是', Boss)