# coding=gbk

text = input('������text�����ݣ�')
words = input('������words�����ݣ�')

#ͳ��
statistics = []

#��������
count_the_words = words.count(' ') + 1

#���ҵĵ���
find_words = []

#�ֿ����ʷ���find_words��
for i in range(count_the_words):
    if words.find(' ') == -1:
        end = len(words)
    else:
        end = words.find(' ')
    find_words.append(words[:end])
    words = words[end + 1:]

#��text�в��ҵ���
for j in range(count_the_words):

    #�����������ж��ٸ��ظ�ֵ
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