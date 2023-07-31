# coding=gbk

words = input('请输入一个由字母构成的字符串：')

for i in range(1, len(words)):
    if (len(words) % len(words[:i]) == 0) and (words.replace(words[:i], '') == ''):
        print(True)
        break

else:
    print(False)