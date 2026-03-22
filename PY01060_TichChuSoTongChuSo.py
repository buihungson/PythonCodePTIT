for _ in range(int(input())):
    n = input()
    tong = 0
    tich = 1
    for i in range(len(n)):
        if i % 2 == 0:
            if n[i] != '0':
                tich *= int(n[i])
        else:
            tong += int(n[i])
    print(tich, tong, sep=" ")