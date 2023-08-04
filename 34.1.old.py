# coding=gbk

word = input('请输入一个英文句子:')
output = []
cache = ''
space = False

for i in range(len(word)):
    if i == 0:
        #如果第一个字符是空格
        if word[0] == ' ':
            continue
        #如果第一个字符不是空格
        else:
            cache = ''.join(word[i])
            continue

    #如果上一个字符是空格并且这个字符不是空格
    if (word[i - 1] == ' ') and (word[i] != ' '):
        cache = ''.join(cache + word[i])
        continue
    #如果上一个字符是字符并且这个字符是空格
    elif (word[i - 1] != ' ') and (word[i] == ' '):
        if space:
            output.append(cache)
        else:
            output.append(cache)
            space = True

        cache = ''
        continue
    #如果上一个字符是字符并且这个字符也是字符
    elif (word[i - 1] != ' ') and (word[i] != ' '):
        cache = ''.join(cache + word[i])

    #如果这个字符是最后一个字
    if i == len(word) - 1:
        output.append(cache)

    #如果这个字符是空格
    elif word[i] == ' ':
        continue

output.reverse()

for i in range(len(output)):
    print(output[i], end = '')
    if i != len(output) - 1:
        print(end = ' ')