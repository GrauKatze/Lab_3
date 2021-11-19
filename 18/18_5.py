# y=kx+b
def equation(a,b):
    a1 = list()
    a2 = list()
    st = a
    for i in range(len(st)):
        if st[i]==";":
            a1.append(float(st[:i]))
            a1.append(float(st[i+1:]))
            break
    st = b
    for i in range(len(st)):
        if st[i]==";":
            a2.append(float(st[:i]))
            a2.append(float(st[i+1:]))
            break
    if a1[0]==a2[0]:
        print(a1[0])
        exit()
    if a1[1]==a2[1]:
        print(a1[1])
        exit()
    k = (a2[1]-a1[1])/(a2[0]-a1[0])
    c = a1[1]/k*a1[0]
    print(k,c)