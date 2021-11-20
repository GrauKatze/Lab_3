hours = dict()
def do_bet(num,coin):
    if coin>0:
        if num not in hours:
            hours[num]=coin
            return "Ваша ставка в размере "+str(coin)+" на лошадь "+str(num)+" принята"
    return "Возникла ошибка, повторите пожалуйста"