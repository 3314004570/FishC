# coding=gbk

name = []       #��Ӱ����
days = []       #��ӳ����
director = []   #��������
performer = []  #��Ա����
score = []      #��Ӱ����
count = 0       #��Ӱ����
choice = ''     #�û�ѡ��

print('��ӭ������CӰ��С����')
print('1.����¼��')
print('2.��ѯ����')
print('3.�˳�����')
func = int(input('��������Ҫ�Ĺ���(1/2/3):'))

while True:
    if func == 1:
        while True:
            name.append(input('�������Ӱ����:'))
            days.append(input('��������ӳ����:'))
            director.append((input('�����뵼������(��������/�ָ�):')).split('/'))
            performer.append((input('��������Ա����(��������/�ָ�):')).split('/'))
            score.append(input('�������Ӱ����:'))
            count += 1
            choice = input('�����Ƿ����¼��(Y/N):')
            if choice == 'Y':
                continue
            else:
                break

    elif func == 2:
        find = input('�������Ӱ����:')
        for i in range(len(name)):
            if name[i].find(find) != -1:
                print(f'��Ӱ����:{name[i]}')
                print(f'��ӳ����:{days[i]}')
                print(f'��������:{director[i]}')
                print(f'��Ա����:{performer[i]}')
                print(f'��ǰ����:{score[i]}')

            elif i == len(name) - 1:
                print('���޴�Ƭ��')

    else:
        break

    func = int(input('\n��������Ҫ�Ĺ���(1/2/3):'))