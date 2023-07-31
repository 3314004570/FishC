# coding=gbk

colors = ["BLACK", "WHITE"]
sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]

result = [[i, j] for i in colors for j in sizes]

print(result)