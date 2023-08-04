# coding=gbk

info = {}

print('欢迎进入鱼C电话簿')
code = input('请输入命令(I:录入/C:查询/D:删除/P:打印/E:退出):')

while True:
    if code == 'I':
        print('\n-- 录入模式 --')
        while True:
            name = input('请输入姓名:')
            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    print(f'该姓名已录入，手机号码是:{info[name]}')
                    if input('请问是否修改(Y/N):') == 'Y':
                        info[name] = input('请输入新的手机号码:')
                    break
            else:
                phone = input('请输入手机号码:')
                if (len(phone) == 11) and (phone.isnumeric()):
                    info[name] = phone
                else:
                    while (len(phone) != 11) or not(phone.isnumeric()):
                        phone = input('输入不合法，请重新输入:')

                    info[name] = phone
            if input('是否继续录入(Y/N):') == 'N':
                break
        
    elif code == 'C':
        print('\n-- 查询模式 --')
        while True:
            name = input('请输入姓名:')
            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    print(f'{name}:{info[name]}')
                    break
            else:
                print('未找到该用户!!!')

            if input('是否继续查询(Y/N):') == 'N':
                break
    elif code == 'D':
        print('\n-- 删除模式 --')
        while True:
            name = input('请输入姓名:')

            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    del(info[name])
                    break
            else:
                print('未找到该用户!!!')

            if input('是否继续删除(Y/N):') == 'N':
                break

    elif code == 'P':
        print('\n-- 打印模式 --')
        for key,value in info.items():
            print(f'{key}:{value}')

    elif code == 'E':
        break

    code = input('\n请输入命令(I:录入/C:查询/D:删除/P:打印/E:退出):')