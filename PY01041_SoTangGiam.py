for _ in range(int(input())):
    n = input()
    i = 0

    while i < len(n)-1 and n[i] < n[i+1]:
        i += 1

    if i == 0 or i == len(n)-1:
        print("NO")
        continue
    while i < len(n)-1 and n[i] > n[i+1]:
        i += 1
    if i != len(n)-1:
        print("NO")
    else:
        print("YES")
