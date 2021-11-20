import math

x = 0.75
y = 0

for t in range(0, math.pi, math.pow(10, -4)):
    if  x==math.pow(math.cos(t),3) and y == math.pow(math.sin(t),3):
        print(t)
        break
