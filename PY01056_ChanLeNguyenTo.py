from math import *
def prime(a):
    if a < 2: return False
    for i in range(2, isqrt(a)+1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    s = input()
    tong = sum(map(int, s.strip()))
    if not prime(tong): print("NO")
    else:
        check = True
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] not in "02468":
                    check = False
                    break
            else:
                if s[i] not in "13579":
                    check = False
                    break
        if check: print("YES")
        else: print("NO")