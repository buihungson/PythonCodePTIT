a, K, N = map(int, input().split())

x = (a // K + 1) * K
found = False
while x <= N:
    print(x - a, end=' ')
    found = True
    x += K
if not found:
    print(-1)