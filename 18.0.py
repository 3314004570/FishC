for i in range(100,1000):
    if(pow(i // 100, 3) + pow((i % 100) // 10, 3) + pow(i % 10, 3) == i):
        print(i)
