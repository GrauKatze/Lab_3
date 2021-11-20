import math


def find_farthest_orbit(orbits):
    max_S = (0, 0)
    for i in orbits:
        if math.pi*max_S[0]*max_S[1] < math.pi*i[0]*i[1]:
            max_S[0], max_S[1] = i[0], i[1]

    return max_S
