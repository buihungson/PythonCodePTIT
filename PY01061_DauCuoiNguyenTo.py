from math import *

def prime(a):
    if a < 2: return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    d = s[:3]
    c = s[-3:]
    if prime(int(d)) and prime(int(c)): print("YES")
    else: print("NO")
