# coding=gbk

set_words = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
put_words = []

for k in range(len(words)):
    for j in range(len(set_words)):
        for i in range(len(words[k])):
            if set_words[j].count(words[k][i]) > 0:
                continue
            else:
                break
        else:
            put_words.append(words[k])
            break

print(put_words)