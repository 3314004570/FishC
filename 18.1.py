num = input('请输入一个正整数：')

if int(num) < 0:
    print('不是回文数')

elif int(num) < 10:
    print('是回文数')

else:
    i = 0
    k = len(num) - 1
    for j in range(len(num) // 2):
        if(num[i] != num[k]):
            print('不是回文数')
            break
        i += 1
        k -= 1

    else:
        print('是回文数')
