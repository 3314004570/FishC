# coding=gbk

i = 0

get_in = input('�������ѹ���ַ���:')
in_length = len(get_in)

while i < len(get_in) - 1:
    if get_in.count(get_in[i]) > 2:
        get_in = "".join(get_in[:i] + get_in[i] + str(get_in.count(get_in[i])) + get_in[i + get_in.count(get_in[i]):])

    i += 1

print('ѹ������ַ���:', get_in)
print(f'ѹ����Ϊ:{(1-len(get_in) / in_length):.2%}')