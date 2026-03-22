for _ in range(int(input())):
    n = input()
    ok = True

    for i in n:
        if i not in "012":
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
