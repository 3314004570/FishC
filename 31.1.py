# coding=gbk

words = input('������Ӣ����ĸ�����ֵ�����ַ���:')
digit = 0
alpha = 0

for i in range(len(words)):
    if words[i].isdigit() == True:
        digit += 1
    elif words[i].isalpha() == True:
        alpha += 1
    else:
        print('������ĸ�����֣�')
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
    print('�ַ��������ֺ���ĸ���������������¸�ʽ��������')