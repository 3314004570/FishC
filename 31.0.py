# coding=gbk

words = input('请输入单词(以回车键结束输入):')

if len(words) == 0:
    print(0)
else:
    print(words.count(' ') + 1)