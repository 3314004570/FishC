# coding=gbk

word = input('������һ��Ӣ�ľ���:')
output = []
cache = ''
space = False

for i in range(len(word)):
    if i == 0:
        #�����һ���ַ��ǿո�
        if word[0] == ' ':
            continue
        #�����һ���ַ����ǿո�
        else:
            cache = ''.join(word[i])
            continue

    #�����һ���ַ��ǿո�������ַ����ǿո�
    if (word[i - 1] == ' ') and (word[i] != ' '):
        cache = ''.join(cache + word[i])
        continue
    #�����һ���ַ����ַ���������ַ��ǿո�
    elif (word[i - 1] != ' ') and (word[i] == ' '):
        if space:
            output.append(cache)
        else:
            output.append(cache)
            space = True

        cache = ''
        continue
    #�����һ���ַ����ַ���������ַ�Ҳ���ַ�
    elif (word[i - 1] != ' ') and (word[i] != ' '):
        cache = ''.join(cache + word[i])

    #�������ַ������һ����
    if i == len(word) - 1:
        output.append(cache)

    #�������ַ��ǿո�
    elif word[i] == ' ':
        continue

output.reverse()

for i in range(len(output)):
    print(output[i], end = '')
    if i != len(output) - 1:
        print(end = ' ')