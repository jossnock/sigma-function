def sigma(r, n, multiplier, constant):
    sum = 0
    for i in range(r, n+1):
        sum += ((i*multiplier) + constant)
    return sum

print(sigma(1,3,2,3))
print(sigma(-1,2,1/2,-1))