# coding=gbk
import copy

plaintext = list(input('请输入需要加密的明文:'))
cache = copy.deepcopy(plaintext)
need_replace = list(input('请输入需要替换的字符:'))
will_replace = list(input('请输入将要替换的字符:'))

if len(need_replace) != len(will_replace):
    print('需要替换的字符数量必须跟将要替换的字符数量一致!')
else:
    for i in range(len(need_replace)):
        cache[plaintext.index(need_replace[i])] = will_replace[i]


    cache = ''.join(cache)
    print('加密后的密文是:', cache)

    for i in range(len(need_replace)):
        if will_replace.count(will_replace[i]) > 1:
            print('由于替换字符出现冲突，该密文无法解密!')
            break