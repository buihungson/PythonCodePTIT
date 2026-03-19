from math import *
t = int(input())
for i in range(t):
    n, x, m = map(float, input().split())
    ans = log(m/n, 1 + x/100)
    print(ceil(ans))