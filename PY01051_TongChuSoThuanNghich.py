from math import *
def palindrome(a):
    if len(a) <= 1: return False
    if a != a[::-1]: return False
    else: return True

for _ in range(int(input())):
    tong = sum(map(int, input().strip()))
    if palindrome(str(tong)): print("YES")
    else: print("NO")