# coding=gbk

text = input('请输入text的内容：')
words = input('请输入words的内容：')

#统计
statistics = []

#单词数量
count_the_words = words.count(' ') + 1

#查找的单词
find_words = []

#分开单词放入find_words中
for i in range(count_the_words):
    if words.find(' ') == -1:
        end = len(words)
    else:
        end = words.find(' ')
    find_words.append(words[:end])
    words = words[end + 1:]

#在text中查找单词
for j in range(count_the_words):

    #查找输入中有多少个重复值
    count_find_words = 0
    for k in range(len(text) - len(find_words[j]) + 1):
        if text[k:k + len(find_words[j])] == find_words[j]:
            count_find_words += 1

    for i in range(count_find_words):
        if i != 0:
            start = text[end + 1:].find(find_words[j]) + end + 1
        else:
            start = text.find(find_words[j])

        end = start + len(find_words[j]) - 1
        statistics.append([start, end])

statistics.sort()
print(statistics)