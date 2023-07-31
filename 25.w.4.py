# coding=gbk
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print('[', end = '')
for i in range(2, -1, -1):
    
    for j in range(2, -1, -1):
        print(matrix[i][j], end = '')
        if i != 0 or j != 0:
            print(end = ',')
        
print(']')