# coding=gbk

matrix = [[1, 3, 2],
          [5, 4, 6],
          [8, 7, 9]]

print(list(map(sorted, [matrix[i] for i in range(3)])))