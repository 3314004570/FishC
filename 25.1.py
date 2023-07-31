# coding=gbk

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

Row = len(matrix)
Column = len(matrix[0])
times = 0

print(end = '[')

while times != -1:
    up = 0 + times
    now_up = len(matrix) - 2 - times
    down = len(matrix) - times
    now_down = 0 + times
    left = -1 + times
    now_left = len(matrix) - 1 - times
    right = len(matrix[0]) - times
    now_right = 0 + times

    while now_right < right:
        print(matrix[now_down][now_right], end = ',')
        now_right += 1

    if down - up < 2:
        print(']')
        break

    now_down += 1
    now_right -= 1
    while now_down < down:
        print(matrix[now_down][now_right], end = ',')
        now_down += 1

    now_down -= 1
    while now_left > left:
        print(matrix[now_down][now_left], end = ',')
        now_left -= 1

    now_left += 1
    while now_up > up:
        print(matrix[now_up][now_left], end = ',')
        now_up -= 1

    now_up += 1
    right -= 1
    down -= 1
    up -= 1
    left += 1
    times += 1
