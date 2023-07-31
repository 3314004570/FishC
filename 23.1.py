# coding=gbk
m = 3
n = 3

matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]

for i in range(0,m):
    for j in range(0,n):
        if matrix[i][matrix[i].index(min(matrix[i]))] < matrix[j][matrix[i].index(min(matrix[i]))]:
            break
    else:
        print('幸运数字是', min(matrix[i]))