# coding=gbk

word = input('������һ��Ӣ�ľ���:')

word = word.strip()

output = word.split()

output.reverse()

print(' '.join(output))