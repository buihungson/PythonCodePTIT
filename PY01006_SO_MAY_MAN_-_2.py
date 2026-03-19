def check(n):
    while n > 0:
        if n % 10 != 4 and n % 10 != 7:
            return False
        n = n // 10
    return True

t = int(input())
for i in range(t):
    n = int(input())
    if check(n): print("YES")
    else : print("NO")
