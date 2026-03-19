t = int(input())
for _ in range(t):
    n = input()
    a = len(n)
    if int(n[a-1]) == 6 and int(n[a-2]) == 8:
        print("YES")
    else:
        print("NO")