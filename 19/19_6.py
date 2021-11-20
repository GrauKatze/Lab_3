def catalan(n):
    if n == 0:
        return 1
    else:
        num=0
        for i in range(n):
            num += catalan(i)*catalan(n-i-1)
        return num