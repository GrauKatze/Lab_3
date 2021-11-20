import math

def roots_of_quadratic_equation(a, b, c):
    roots = list()
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
        disc = math.pow(b,2)-4*a*c
        if disc < 0:
            roots.append(-1)
        elif disc == 0:
            roots.append(-b/(2*a))
        else:
            roots.append((-b+math.sqrt(disc))/(2*a))
            roots.append((-b-math.sqrt(disc))/(2*a))
    return(roots)