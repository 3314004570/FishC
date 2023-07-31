n = int(input("请输入一个正整数："))

while n > 0:
    if n % 2 == 0:
        print(n,'/ = ',int(n / 2))
        n = int(n / 2)
    else:
        print(n,'* 3 + 1 = ',int(n * 3 + 1))
        n = int(n * 3 + 1)
    if n == 1:
        break

