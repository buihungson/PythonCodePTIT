t = int(input())
for _ in range(t):
    n = input()
    for i in range(0, len(n), 2):
        for j in range(int(n[i+1])):
            print(n[i], end='')
    print()

