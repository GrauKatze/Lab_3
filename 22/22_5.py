import math

def solve(*coefficients):
    roots = list()
    a, b, c = 0
    if 0<len(coefficients)<4:
        if len(coefficients) == 3:
            a = coefficients[0]
            b = coefficients[1]
            c = coefficients[2]
        elif len(coefficients) == 2:
            b = coefficients[0]
            c = coefficients[1]
        elif len(coefficients) == 1:
            c = coefficients[0]
    else:
        return "None"
    
    if a and b and c == 0:
        roots.append("all")
    elif a and b == 0:
        roots.append(-1)
    elif a == 0:
        roots.append(-c/b)
    elif b == 0:
        if c > 0:
            roots.append(-1)
        elif c == 0:
            roots.append(0)
        else:
            roots.append(math.sqrt(c/a))
    elif c == 0:
        roots.append(0)
        roots.append(-b/a)
    else:
        disc = math.pow(b, 2)-4*a*c
        if disc < 0:
            roots.append(-1)
        elif disc == 0:
            roots.append(-b/(2*a))
        else:
            roots.append((-b+math.sqrt(disc))/(2*a))
            roots.append((-b-math.sqrt(disc))/(2*a))
    return(roots)

print(solve(input()))