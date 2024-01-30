def sigma(r, n, multiplier, constant):
    sum = 0
    for i in range(r, n+1):
        sum += ((i*multiplier) + constant)
    return sum

assert(sigma(1,3,2,3)==21)
assert(int(sigma(-1,2,1/2,-1))==-3)
assert(sigma(1,3,1,0)==6)