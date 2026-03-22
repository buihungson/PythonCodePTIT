for _ in range(int(input())):
    n = input()
    tong = 0
    tich = 1
    vtle = 0
    vtle0 = 0

    for i in range(len(n)):
        if i % 2 == 0:
            tong += int(n[i])
        else :
            vtle += 1
            if n[i] != "0":
                tich *= int(n[i])
            else: vtle0 += 1
    print(tong, end=" ")
    if vtle0 == vtle: print("0")
    else: print(tich)