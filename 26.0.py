# coding=gbk

import timeit

list_test = timeit.repeat('a = []', repeat=100)

list_use_time=sum(list_test) / len(list_test)

tuple_test = timeit.repeat('a = ()', repeat=100)

tuple_use_time=sum(tuple_test) / len(tuple_test)

print('����100���б�ƽ����ʱΪ', list_use_time, '��')
print('����100��Ԫ�飬ƽ����ʱΪ', tuple_use_time, '��')

if tuple_use_time > list_use_time:
   print('�����б����')
else:
    print('����Ԫ�����')