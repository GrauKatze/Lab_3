def bracket_check(st):
    check = 0
    if st[0]!=")":
        for i in st:
            if i == "(":
                check+=1
            elif i ==")":
                check-=1
            if check<0:
                break
        if check==0:
            print("yes!")
            exit()
    print("NO")

bracket_check("((())())()")