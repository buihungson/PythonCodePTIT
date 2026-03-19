import math

def isprime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ucln = math.gcd(a, b)
    tong = 0
    for i in str(ucln):
        tong += int(i)
    if isprime(tong): print("YES")
    else: print("NO")