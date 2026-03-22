for _ in range(int(input())):
    check = True
    n = input()
    dem = 0
    if int(n) % 7 == 0:
        print(n)
        check = False

    while check == True:
        m = n[::-1]
        s = int(n) + int(m)
        if s % 7 == 0:
            check = False
            print(s)
        else:
            n = str(s)
            dem += 1
        if dem == 1000:
            print(-1)
            break


