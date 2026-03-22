for _ in range(int(input())):
    n = input()
    if len(set(n)) > 2:
        print("NO")
        continue

    check = True
    for i in range(2, len(n)):
        if n[i] != n[i-2]:
            check = False
            break
    if check: print("YES")
    else:
        print("NO")


