lastTicket = int()


def lucky(ticket):
    if test_lucky_ticket(lastTicket) and test_lucky_ticket(ticket):
        return "Счастливый"
    return "Несчастливый"


def test_lucky_ticket(ticket):
    while len(ticket) < 6:
        ticket = "".join(str(0), ticket)
    if (int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[3])+int(ticket[4])+int(ticket[5])):
        return 1
    return 0
