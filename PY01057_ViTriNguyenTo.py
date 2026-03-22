from math import *

def prime(a):
    if a < 2: return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    check = True
    for i in range(len(s)):
        if prime(int(i)):
            if not prime(int(s[i])):
                check = False
                break
        else:
            if prime(int(s[i])):
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")
