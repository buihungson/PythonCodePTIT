import math
def prime(a):
    if a < 2: return False
    for x in range(2, int(math.sqrt(a))+1):
        if a % x == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    res = "1"

    for i in range(2, int(math.sqrt(n))+1):
        dem = 0
        while n % i == 0:
            n //= i
            dem += 1
        if dem > 0:
            res += f" * {i}^{dem}"
    if n > 1:
        res += f" * {n}^1"
    print(res)