import math
for _ in range(int(input())):
    s = input()
    n = s[::-1]
    s = int(s)
    n = int(n)
    if math.gcd(n, s) != 1: print("NO")
    else: print("YES")
