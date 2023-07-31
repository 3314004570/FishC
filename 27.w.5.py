# coding=gbk

x = ["123", "33211", "12321", "13531", "112233"]
y = []

for i in range(len(x)):
    if x[i] == x[i][::-1]:y.append(x[i])

print(y)