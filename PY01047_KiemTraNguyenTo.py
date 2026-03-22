from math import *
def prime(a):
    if a < 2: return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    n = int(input())
    check = n % 10000
    if prime(check): print("YES")
    else: print("NO")
