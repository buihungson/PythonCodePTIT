for _ in range(int(input())):
    s = input()
    check = True
    if s[0] == s[1]:
        print("NO")
    elif len(s) % 2 == 0:
        print("NO")
    else:
        for i in range(0, len(s)-2, 2):
            if s[i] != s[i+2]:
                check = False
        if check: print("YES")
        else: print("NO")
