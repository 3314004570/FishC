# coding=gbk

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

Row = len(matrix)
Column = len(matrix[0])

print('[', end = '')

for i in range(Column):
    print('[', end = '')
    for j in range(Row):
        print(matrix[j][i], end = '')
        if j != Row - 1:
            print(end = ',')

    if i == Column - 1:
        print(']', end = '')
    else:
        print(']')
print(']', end = '')