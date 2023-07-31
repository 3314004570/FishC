# coding=gbk
import random

findnum = int(input('请输入一个待匹配的整数：'))

matrix = [[0 for i in range(88)] for j in range(88)]

for i in range(0,88):
    for k in range(0,88):
        matrix[i][k] = random.randint(0,1024)
        if findnum == matrix[i][k]:
            print(i,k)