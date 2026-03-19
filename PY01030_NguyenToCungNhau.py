import math
def isCheck(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False
n, k = map(int, input().split())
x1 = 10**(k-1)
x2 = 10**k
cnt = 0
for i in range(x1, x2):
    if isCheck(i, n):
        cnt+=1
        print(i, end = " ")
    if cnt == 10:
        cnt = 0
        print()