# coding=gbk

num = input('������һ�����֣�')

for i in range(1,len(num) + 1):
    if int(list(num)[-i]) % 2 == 1:
        if i == 1:
            print(int(num[:]))
        else:
            print(int(num[:-i + 1]))
        break
else:
    print('0')