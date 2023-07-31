# coding=gbk

ver = []

print(end = '请输入第一个版本号，V1 = ')
word = input()
ver.append(list(word))

print(end = '请输入第二个版本号，V1 = ')
word = input()
ver.append(list(word))

for j in range(2):
    count = ver[j].count('.')
    for i in range(count):
        ver[j].remove('.')

if len(ver[0]) > len(ver[1]):
    for i in range(len(ver[0]) - len(ver[1])):
        ver[1].append('0')
elif len(ver[0]) < len(ver[1]):
    for i in range(len(ver[1]) - len(ver[0])):
        ver[0].append('0')

for i in range(0,2):
    ver[i] = int(''.join(ver[i]))

if int(ver[0]) > int(ver[1]):
    print('V1')
elif int(ver[0]) < int(ver[1]):
    print('V2')
else:
    print('V1 = V2')