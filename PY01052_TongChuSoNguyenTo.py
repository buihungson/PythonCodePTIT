from math import *
def prime(a):
    if a < 2:
        return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0: return False
    return True
for _ in range(int(input())):
    s = input()
    tong = sum(map(int, s.strip()))
    if prime(tong): print("YES")
    else: print("NO")