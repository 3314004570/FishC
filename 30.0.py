# coding=gbk

plaintext = input('��������Ҫ���ܵ����ģ�ֻ֧��Ӣ����ĸ����')
digit = int(input('�������ƶ���λ����'))

for i in range(len(plaintext)):
    #ΪСд��ĸ
    if (ord(plaintext[i]) <= 122) and (ord(plaintext[i]) >= 97):
        if ord(plaintext[i]) + digit <= 122:
            print(chr(ord(plaintext[i]) + digit), end = '')
        else:
            print(chr(ord(plaintext[i]) + digit - 26), end = '')
    #Ϊ��д��ĸ
    elif (ord(plaintext[i]) <= 90) and (ord(plaintext[i]) >= 65):
        if ord(plaintext[i]) + digit <= 90:
            print(chr(ord(plaintext[i]) + digit), end = '')
        else:
            print(chr(ord(plaintext[i]) + digit - 26), end = '')

    else:
        print(plaintext[i], end = '')