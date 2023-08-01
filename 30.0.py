# coding=gbk

plaintext = input('请输入需要加密的明文（只支持英文字母）：')
digit = int(input('请输入移动的位数：'))

for i in range(len(plaintext)):
    #为小写字母
    if (ord(plaintext[i]) <= 122) and (ord(plaintext[i]) >= 97):
        if ord(plaintext[i]) + digit <= 122:
            print(chr(ord(plaintext[i]) + digit), end = '')
        else:
            print(chr(ord(plaintext[i]) + digit - 26), end = '')
    #为大写字母
    elif (ord(plaintext[i]) <= 90) and (ord(plaintext[i]) >= 65):
        if ord(plaintext[i]) + digit <= 90:
            print(chr(ord(plaintext[i]) + digit), end = '')
        else:
            print(chr(ord(plaintext[i]) + digit - 26), end = '')

    else:
        print(plaintext[i], end = '')