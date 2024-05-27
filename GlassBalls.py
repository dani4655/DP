import numpy as np
# q1 calculate the minimal value for checks needed for n floors with k crystal balls
# <=> get the max floors possible with m tries and k balls
def checking_number(n: int, k: int) -> int:
    min = 0
    binom = [0] * (k + 1)
    for i in range(1, n+1):
        if binom[k]>=n:
            break
        min = min + 1
        for x in range(k, 0, -1):
            binom[x] = 1 + binom[x] + binom[x - 1] #the recursive formula from the pdf
    return min


#q2 find the first floor which the ball will break at using optimal search algorithm
def index_floor(f_i: list[int], b: int) -> int:
    n = len(f_i)
    up = index_first_floor(n) - 1
    down = 0
    k = 2
    step = up
    if not breaks(f_i[n-1], b):
        return -1
    while k>0:
        if breaks(f_i[up], b):
            k-=1
            for i in range(down,up+1):
                if breaks(f_i[i], b):
                    return i+1
        else:
            down = up
            step = step -1
            if step == 0:
                step = 1
            up = up + step



def breaks(n :int, b: int):
    if b < n:
        return True
    return False

#q3 find the first floor to start looking with the optimal algorithm
def index_first_floor(n: int) -> int:
    a, b = np.roots([1, 1, -2*n])
    ans = max(a, b)
    return int(np.ceil(ans))


