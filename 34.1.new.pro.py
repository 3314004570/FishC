# coding=gbk

word = input('请输入一个英文句子:')

print(' '.join(word.strip().split()[::-1]))