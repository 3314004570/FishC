# coding=gbk
import copy

plaintext = list(input('��������Ҫ���ܵ�����:'))
cache = copy.deepcopy(plaintext)
need_replace = list(input('��������Ҫ�滻���ַ�:'))
will_replace = list(input('�����뽫Ҫ�滻���ַ�:'))

if len(need_replace) != len(will_replace):
    print('��Ҫ�滻���ַ������������Ҫ�滻���ַ�����һ��!')
else:
    for i in range(len(need_replace)):
        cache[plaintext.index(need_replace[i])] = will_replace[i]


    cache = ''.join(cache)
    print('���ܺ��������:', cache)

    for i in range(len(need_replace)):
        if will_replace.count(will_replace[i]) > 1:
            print('�����滻�ַ����ֳ�ͻ���������޷�����!')
            break