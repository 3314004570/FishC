money = int(input('请输入今年的利润:'))

if money <= 100000:
    should_pay = money * 0.1
elif money <= 200000:
    should_pay = 10000 + (money - 100000) * 0.075
elif money <= 400000:
    should_pay = 10000 + 7500 + (money - 200000) * 0.05
elif money <= 600000:
    should_pay = 10000 + 7500 + 10000 + (money - 400000) * 0.03
elif money <= 1000000:
    should_pay = 10000 + 7500 + 10000 + 6000 + (money - 400000) * 0.015
else:
    should_pay = 10000 + 7500 + 10000 + 6000 + 6000 + (money - 1000000) * 0.01

print('应该发放的奖金总数是:', should_pay)
