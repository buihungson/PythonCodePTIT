from math import *
def prime(a):
    if int(a) < 2: return False
    for i in range(2, isqrt(int(a))+1):
        if int(a) % i == 0: return False
    return True

for _ in range(int(input())):
    n = input()
    if prime(len(n)) == False:
        print("NO")
    else:

        m = int(n)
        pr = 0
        npr = 0

        while m != 0:
            tmp = m % 10
            m //= 10
            if prime(tmp): pr += 1
            else: npr += 1

        if pr >= npr: print("YES")
        else: print("NO")

