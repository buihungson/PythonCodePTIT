n = int(input())
tmp1 = 0
tmp2 = 0
while n > 0:
        if n % 10 == 4:
            tmp1 = tmp1 + 1
        elif n % 10 == 7:
            tmp2 = tmp2 + 1
        n = n // 10
ans = tmp1 + tmp2

if (ans == 4) or (ans == 7): print("YES")
else : print("NO")