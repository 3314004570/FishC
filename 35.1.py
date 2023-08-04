# coding=gbk

times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]
usetime = []
minimum = []
maxmum = []
miniout = []
maxout = []

for i in range(len(times)):
    if i == 0:
        usetime.append(times[i])
    else:
        usetime.append(times[i] - times[i - 1])

i = 0
mincache = usetime.copy()
while True:
    minimum.append(min(mincache))
    miniout.append(names[mincache.index(minimum[i])])
    mincache[mincache.index(min(mincache))] = max(mincache)
    i += 1
    if min(mincache) != minimum[i - 1]:
        break
print('速度最快的是:', miniout, '耗费的时间是:', minimum[0])

i = 0
maxcache = usetime.copy()
while True:
    maxmum.append(max(maxcache))
    maxout.append(names[maxcache.index(maxmum[i])])
    maxcache[maxcache.index(max(maxcache))] = min(maxcache)
    i += 1
    if max(maxcache) != maxmum[i - 1]:
        break
print('速度最慢的是:', maxout, '耗费的时间是:', maxmum[0])