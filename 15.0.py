beer = int(input('请输入血液酒精含量:'))

if beer <  20:
    print('不构成饮酒行为')
elif beer < 80:
    print('构成酒后驾驶')
elif beer >= 80:
    print('构成醉酒驾驶')
