# coding=gbk

word = input('请输入一个英文句子:')

word = word.strip()

output = word.split()

output.reverse()

print(' '.join(output))