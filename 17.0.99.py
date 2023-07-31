first = 1
last = 1

while last <= 9:
    while first <= last:
        print(first, 'x', last, '=', first * last, ' ', end='')
        first += 1

    first = 1
    last += 1
    print('')
