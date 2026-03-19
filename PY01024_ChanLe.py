def check(a):
    s = 0
    for i in a:
        s += int(i)
    if s % 10 != 0: return False
    for i in range(len(a)-1):
        if abs(int(a[i]) - int(a[i+1])) != 2: return False
    return True
for _ in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")