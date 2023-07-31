i = 1
sum = 0

while i <= 64:
    wheats = pow(2, i - 1)
    sum = sum + wheats
    i = i + 1

print("舍罕王应该给达依尔", sum, "粒麦子！")
