# coding=gbk

i = 0
j = 0

s = input('�������ַ���s:')
t = input('�������ַ���t:')

same_times = 0

while i < len(s):
    while j < len(t):
        if s[i] == t[j]:
            same_times += 1
            break
        j += 1

    i += 1
if same_times == len(s):
    print('�ַ���s���ַ���t�������С�')
else:
    print('�ַ���s�����ַ���t�������С�')