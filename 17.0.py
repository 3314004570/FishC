first = 9
last = 1

while last <= 9:
    while first >= last:
        print(first, '*', last, '=', first * last, ' ', end='')
        first -= 1

    first = 9
    last += 1
    print('')
