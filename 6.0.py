score = int(input('请输入你的分数:'))
if score < 60:
    print('D')

else:
    if 60 <= score < 80:
        print('C')

    else:
        if 80 <= score < 90:
            print('B')

        else:
            if 90 <= score < 100:
                print('A')

            else:
                if score == 100:
                    print('S')
    
