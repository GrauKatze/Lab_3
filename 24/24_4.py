num = input()
words_list = list()
end_list = list()
for i in range(num):
    words_list.append(input())

for i in range(0, words_list):
    var_list = list()
    var_list.append(words_list(i))
    word = words_list[i].split()
    for j in range(i, words_list):
        if word.upper() == words_list[j].split().upper():
            var_list.append(words_list[j])
            words_list.extend(j)
    end_list.append(var_list)
