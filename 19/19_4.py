def palindrome(s):
    sp = s.split()
    s = ''.join(sp)
    for i in range(1,len(s)):
        if s[i-1]!=s[-i]:
            return("NO")
    return("Yes")