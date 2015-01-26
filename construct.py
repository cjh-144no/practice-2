import math,random

def construct_array(n,m):
    x = []
    for i in range(m):
        r = random.random()
        y = n*r
        x.append(math.floor(y))
    return x
