alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
new_msg = list()


def encrypt_ceaser(msg, shift):
    shift = int(shift)
    for i in msg:
        if i in alph:
            for j in range(len(alph)):
                if alph[j] == i:
                    new_msg.append(alph[(j+shift) % len(alph)])
                    continue
        if i in alph.lower():
            for j in range(len(alph)):
                if alph[j].lower() == i:
                    new_msg.append(alph[(j+shift) % len(alph)].lower())
                    continue
        new_msg.append(i)
    return str("".join(new_msg))


def decrypt_ceaser(msg, shift):
    shift = int(shift)
    for i in msg:
        if i in alph:
            for j in range(len(alph)):
                if alph[j] == i:
                    new_msg.append(alph[(j-shift)])
                    continue
        if i in alph.lower():
            for j in range(len(alph)):
                if alph[j].lower() == i:
                    new_msg.append(alph[(j-shift)].lower())
                    continue
        new_msg.append(i)
    return str("".join(new_msg))
