words = list()
words.append(input())
dict_words = dict()
gema_list = list()


for i in words:
    gematria = 0
    for j in i.upper():
        gematria += ord(j)
    dict_words[gematria] = i
    gema_list.append(gematria)

gema_list.sort()
for i in gema_list:
    print(dict_words[i])