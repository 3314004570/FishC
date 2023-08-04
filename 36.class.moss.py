# coding=gbk

dictionary = (('.-', '-...', '-.-.', '-..', '.',
              '..-.', '--.', '....', '..', '.---', 
              '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', 
             '..-', '...-', '.--', '-..-', '-.--', '--..', 
             '.----', '..---', '...--', '....-', '.....', 
             '-....', '--...', '---..', '----.', '-----'),
              ('A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 
              'O', 'P', 'Q', 'R', 'S', 'T', 
              'U', 'V', 'W', 'X', 'Y', 'Z', 
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

cache = ''
split = []

mos = input('请输入摩斯密码(每个字符的摩斯密码之间以空格为间隔)：')

for i in range(len(mos)):
    if mos[i] != ' ':
        if i != len(mos) - 1:
            cache = ''.join(cache + mos[i])
        else:
            cache = ''.join(cache + mos[i])
            split.append(cache)
            break
        
    else:
        split.append(cache)
        cache = ''


for i in range(len(split)):
    print(dictionary[1][(dictionary[0].index(split[i]))], end = '')