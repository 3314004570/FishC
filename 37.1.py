# coding=gbk

info = {}

print('��ӭ������C�绰��')
code = input('����������(I:¼��/C:��ѯ/D:ɾ��/P:��ӡ/E:�˳�):')

while True:
    if code == 'I':
        print('\n-- ¼��ģʽ --')
        while True:
            name = input('����������:')
            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    print(f'��������¼�룬�ֻ�������:{info[name]}')
                    if input('�����Ƿ��޸�(Y/N):') == 'Y':
                        info[name] = input('�������µ��ֻ�����:')
                    break
            else:
                phone = input('�������ֻ�����:')
                if (len(phone) == 11) and (phone.isnumeric()):
                    info[name] = phone
                else:
                    while (len(phone) != 11) or not(phone.isnumeric()):
                        phone = input('���벻�Ϸ�������������:')

                    info[name] = phone
            if input('�Ƿ����¼��(Y/N):') == 'N':
                break
        
    elif code == 'C':
        print('\n-- ��ѯģʽ --')
        while True:
            name = input('����������:')
            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    print(f'{name}:{info[name]}')
                    break
            else:
                print('δ�ҵ����û�!!!')

            if input('�Ƿ������ѯ(Y/N):') == 'N':
                break
    elif code == 'D':
        print('\n-- ɾ��ģʽ --')
        while True:
            name = input('����������:')

            for i in range(len(info)):
                if info.get(name, 0) != 0:
                    del(info[name])
                    break
            else:
                print('δ�ҵ����û�!!!')

            if input('�Ƿ����ɾ��(Y/N):') == 'N':
                break

    elif code == 'P':
        print('\n-- ��ӡģʽ --')
        for key,value in info.items():
            print(f'{key}:{value}')

    elif code == 'E':
        break

    code = input('\n����������(I:¼��/C:��ѯ/D:ɾ��/P:��ӡ/E:�˳�):')