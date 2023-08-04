# coding=gbk

cache = ''
Caesar = ''
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

plaintext = input('请输入明文:')
digit = int(input('请输入移动的位数:'))

for i in range(len(plaintext)):
    #为小写字母
    if (ord(plaintext[i]) <= 122) and (ord(plaintext[i]) >= 97):
        if ord(plaintext[i]) + digit <= 122:
            Caesar = ''.join(Caesar + chr(ord(plaintext[i]) + digit))
        else:
            Caesar = ''.join(Caesar + chr(ord(plaintext[i]) + digit - 26))
    #为大写字母
    elif (ord(plaintext[i]) <= 90) and (ord(plaintext[i]) >= 65):
        if ord(plaintext[i]) + digit <= 90:
            Caesar = ''.join(Caesar + chr(ord(plaintext[i]) + digit))
        else:
            Caesar = ''.join(Caesar + chr(ord(plaintext[i]) + digit - 26))

    else:
        Caesar = ''.join(Caesar + plaintext[i])

print(f'凯撒加密后的密文是:{Caesar}')

for i in range(len(Caesar)):
    if Caesar[i] != ' ':
        if i != len(Caesar) - 1:
            
            cache = ''.join(cache + dictionary[0][(dictionary[1].index(Caesar[i].upper()))] + ' ')
        else:
            cache = ''.join(cache + dictionary[0][(dictionary[1].index(Caesar[i].upper()))])
            break
    else:
        cache = ''.join(cache + ' ')

print(f'凯撒、摩斯混合加密后的密文是{cache}:', end = '')