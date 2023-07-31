# coding=gbk

import timeit

list_test = timeit.repeat('a = []', repeat=100)

list_use_time=sum(list_test) / len(list_test)

tuple_test = timeit.repeat('a = ()', repeat=100)

tuple_use_time=sum(tuple_test) / len(tuple_test)

print('创建100次列表，平均用时为', list_use_time, '秒')
print('创建100次元组，平均用时为', tuple_use_time, '秒')

if tuple_use_time > list_use_time:
   print('创建列表更快')
else:
    print('创建元组更快')