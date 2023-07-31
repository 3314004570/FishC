# coding=gbk

result = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(result)