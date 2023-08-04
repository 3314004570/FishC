# coding=gbk

name = {}       #电影名称
days = {}       #上映日期
director = {}   #导演名字
performer = {}  #演员名字
score = {}     #电影评分
count = 0       #电影数量
choice = ''     #用户选择

print('欢迎进入鱼C影评小程序')
print('1.数据录入')
print('2.查询数据')
print('3.退出程序')
func = int(input('请输入想要的功能(1/2/3):'))

while True:
    if func == 1:
        while True:
            name[count] = input('请输入电影名称:')
            days[count] = input('请输入上映日期:')
            director[count] = (input('请输入导演名字(多人请用/分隔):')).split('/')
            performer[count] = (input('请输入演员名字(多人请用/分隔):')).split('/')
            score[count] = input('请输入电影评分:')
            count += 1
            choice = input('请问是否继续录入(Y/N):')
            if choice == 'Y':
                continue
            else:
                break

    elif func == 2:
        find = input('请输入电影名称:')
        for i in range(len(name)):
            if name[i] == find:
                print(f'电影名称:{name[i]}')
                print(f'上映日期:{days[i]}')
                print(f'导演名单:{director[i]}')
                print(f'演员名单:{performer[i]}')
                print(f'当前评分:{score[i]}')
                break

            elif i == len(name) - 1:
                print('查无此片！')

    else:
        break

    func = int(input('\n请输入想要的功能(1/2/3):'))