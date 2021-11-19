# y=kx+b
def line(s, t):
    for i in range(len(s)):
        if s[i] == "x":
            k = float(s[:i])
            b = float(s[i+2:])
            break
    for i in range(len(t)):
        if t[i] == ";":
            x = float(t[:i])
            y = float(t[i+1:])
            break
    if y == k*x+b:
        print("yes")
        exit()
    print("no")


line("1x+6", "1;7")
