# coding=gbk

words = input('������һ������ĸ���ɵ��ַ�����')

for i in range(1, len(words)):
    if (len(words) % len(words[:i]) == 0) and (words.replace(words[:i], '') == ''):
        print(True)
        break

else:
    print(False)