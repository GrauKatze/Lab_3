base = list()

def hello(name):
    print("Здравствуйте, "+str(name)+"! Вашу карту ищут...")
def search_card(name):
    ans = "не"
    for i in range(len(base)):
        if name == base[i]:
            ans = str(i+1)
            break            
    print("Ваша карта с номером "+ans+" найдена")