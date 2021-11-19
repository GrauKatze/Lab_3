def possible_turns(coord):
    bykv = "ABCDEFGH"
    for i in range(8):
        if coord[0] == bykv[i]:
            x = i
            break
    y = int(coord[1])
    hod = list()

    if y + 2 < 8:
        if x+1 < 8:
            hod.append((bykv[x+1], y+2))
        if x-1 >= 0:
            hod.append((bykv[x-1], y+2))
    if y - 2 > 0:
        if x+1 < 8:
            hod.append((bykv[x+1], y-2))
        if x-1 >= 0:
            hod.append((bykv[x-1], y-2))
    if x + 2 < 8:
        if y+1 < 8:
            hod.append((bykv[x+2], y+1))
        if y-1 > 0:
            hod.append((bykv[x+2], y-1)) 
    if x - 2 >= 0:
        if y+1 < 8:
            hod.append((bykv[x-2], y+1))
        if y-1 > 0:
            hod.append((bykv[x-2], y-1))
    print(hod)

possible_turns("H8")