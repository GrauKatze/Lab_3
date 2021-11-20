translateText = None

def translate(text):
    global translateText
    word = str()
    for i in text:
        if i not in 'аиеёоуыэюя':
            word += i
    translateText = word