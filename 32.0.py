# coding=gbk

i = 0

get_in = input('请输入待压缩字符串:')
in_length = len(get_in)

while i < len(get_in) - 1:
    if get_in.count(get_in[i]) > 2:
        get_in = "".join(get_in[:i] + get_in[i] + str(get_in.count(get_in[i])) + get_in[i + get_in.count(get_in[i]):])

    i += 1

print('压缩后的字符串:', get_in)
print(f'压缩率为:{(1-len(get_in) / in_length):.2%}')