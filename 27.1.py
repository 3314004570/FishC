# coding=gbk

s = input('请输入规定的序列：')

for i in range(0, len(s), 2):
    if ord(s[i]) + int(s[i + 1]) <= 122:
        s = s[0:i + 1] + chr(ord(s[i]) + int(s[i + 1])) + s[i + 2:len(s)]
    else:
        s = s[0:i + 1] + chr(ord(s[i]) + int(s[i + 1]) - 26) + s[i + 2:len(s)]

print('转换后的序列为：', s)