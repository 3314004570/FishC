# coding=gbk

words = input('请输入英文字母加数字的组合字符串:')
digit = 0
alpha = 0

for i in range(len(words)):
    if words[i].isdigit() == True:
        digit += 1
    elif words[i].isalpha() == True:
        alpha += 1
    else:
        print('不是字母或数字！')
        break

if digit - alpha == -1:
    half = int(len(words) / 2)
    print(words[0], end = '')

    for i in range(1, half + 1):
        print(words[half + i], end = '')
        print(words[i], end = '')

elif digit - alpha == 1:
    half = int(len(words) / 2)
    print(words[half], end = '')

    for i in range(0, half):
        print(words[i], end = '')
        print(words[half + i + 1], end = '')
else :
    print('字符串中数字和字母的数量不满足重新格式化的条件')