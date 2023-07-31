import random

red = random.sample(range(1, 33), 6)
blue = random.randint(1,16)
print('开奖结果是:', *red)
print('特别号码是:', blue)
