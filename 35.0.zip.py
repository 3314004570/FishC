# coding=gbk

a = [1,2,3]
b = [4,5,6]

for i in range(min(len(a), len(b))):
    print(a[i], ',', b[i])