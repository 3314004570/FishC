# coding=gbk

words = input('�����뵥��(�Իس�����������):')

if len(words) == 0:
    print(0)
else:
    print(words.count(' ') + 1)