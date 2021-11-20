def month_name(num, lang):
    month_ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    month_en = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
    if lang == "ru":
        return(month_ru[num-1])
    elif lang == "en":
        return(month_en[num-1])
