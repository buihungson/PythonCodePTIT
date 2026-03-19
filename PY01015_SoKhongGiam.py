t = int(input())
for _ in range(t):
    n = input()
    dem = 0
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            dem += 1
            break
    if dem == 0:
        print("YES")
    else:
        print("NO")
