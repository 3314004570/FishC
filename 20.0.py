is_print = 0
char = input('请输入测试字符串：')

times = 0
words = []

while times < 6:
    words[times] = char[times]

#判断有没有6个字符
if len(words) != 6:
    print('非法T_T,不是6个字')
    is_print = 1

#判断六个字符是不是要求的字符
if is_print != 1:    
    times = 0
    while times < 6:
        if words[times] == '{' or words[times] == '}' or words[times] == '[' or words[times] == ']' or words[times] == '(' or words[times] == ')':
            times += 1
            
        #有不符合要求的字符
        else:
            print('非法T_T, 有不符合要求的字符串')
            is_print = 1

    #没有不符合要求的字符
    if is_print != 1:
        k = 0
        i = 0
        
        #把右括号转换为左括号
        while k < 6:
            if words[k] == '}':
                words[k] = '{'
                i += 1

            elif words[k] == ']':
                words[k] = '['
                i += 1

            elif words[k] == ')':
                words[k] = '('
                i += 1

            k += 1
        
        #转换次数不足三次为不合法
        if i != 3:
            print('非法T_T')
            is_print = 1

        print('转换完成的char=',words)
        #转换次数为3次
        if is_print != 1:
            if words[0] == words[1]:
                if (words[2] == words[3] and words[4] == words[5]) or (words[2] == words[5] and words[3] == words[4]):
                    print('合法^o^')
                else:
                    print('非法T_T')
                
            elif words[0] == words[3]:
                if words[1] == words[2] and words[4] == words[5]:
                    print('合法^o^')
                else:
                    print('非法T_T')
                    
            elif words[0] == words[5]:
                if (words[1] == words[2] and words[3] == words[4]) or (words[1] == words[4] and words[2] == words[3]):
                    print('合法^o^')
                else:
                    print('非法T_T')
                
            else:
                print('非法T_T')
                is_print = 1
