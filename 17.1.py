first = 2
last = 2
num = 2
isprint = 0

while num <= 9:
    first = 2
    isprint = 0
    while first < num:
        last = first
        while last < num:
            if first * last == num:
                print(first * last, '=', first, '*', last)
                isprint = 1
                break;
            else:
                last += 1
                
        first += 1

    if isprint == 0:
        print(num, '是一个素数')
        
    num += 1
        
