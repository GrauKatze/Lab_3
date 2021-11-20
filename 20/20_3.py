spisok_umor = list()
def print_only_new(text):
    global spisok_umor
    if int(text[12:]) not in spisok_umor:
        spisok_umor.append(int(text[12:]))
        print(text)
