Name = str()
Data = str()


def setup_profile(name, data):
    global Name
    Name = name
    global Data
    Data = data


def print_application_for_leave():
    print("Заявление на отпуск в период "+Data + ". "+Name)


def print_holiday_money_claim(amount):
    print("Прошу выплатить мне "+amount + " отпускных денег. "+Name)


def print_attorney_letter(toWhom):
    print("На время отупска в пероид "+Data+"мои заместителем будет "+toWhom+". "+Name)