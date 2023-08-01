# coding=gbk

get_in = input('请输入待解压字符串:')
get_out = ''.join(get_in)
sum_add = 0

i = 0

while 1:
    if get_in[i].isdigit() == True:
        get_out = ''.join(get_out[:i - 1 + sum_add])
        get_out = ''.join(get_out + get_in[i - 1] * int(get_in[i]))
        sum_add = int(get_in[i]) - 2
        get_out = ''.join(get_out + get_in[i + 1:])

    i += 1

    if i == len(get_in):
        break

print(get_out)