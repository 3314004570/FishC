# coding=gbk

i = 0
j = 0

s = input('请输入字符串s:')
t = input('请输入字符串t:')

same_times = 0

while i < len(s):
    while j < len(t):
        if s[i] == t[j]:
            same_times += 1
            break
        j += 1

    i += 1
if same_times == len(s):
    print('字符串s是字符串t的子序列。')
else:
    print('字符串s不是字符串t的子序列。')