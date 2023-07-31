score = input('请输入你的分数:')

while score != 'e':

    if int(score) < 60:
        print('D')

    else:
        if 60 <= int(score) < 80:
            print('C')

        else:
            if 80 <= int(score) < 90:
                print('B')

            else:
                if 90 <= int(score) < 100:
                    print('A')

                else:
                    if int(score) == 100:
                        print('S')

    score = input('请输入你的分数:')
    
