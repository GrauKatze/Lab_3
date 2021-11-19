def ask_password():
    pas = "password"
    for i in range(0,3):
        if pas == input():
            print("Пароль принят")
            exit(0)
    print("В доступе отказано")
    