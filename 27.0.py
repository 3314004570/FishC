# coding=gbk

s = input('��������������ַ���:')
s_length = len(s)
j = 0

while j < s_length - 1:
    if (s[j] != s[j + 1]) and (s[j].upper() == s[j + 1].upper()):
        cache = list(s)
        cache.pop(j)
        cache.pop(j)
        s = "".join(cache)
        s_length -= 2
        j = -1
    j += 1

print('�������ַ���:', s)