for _ in range(int(input())):
    tich = 1
    n = int(input())
    while n > 0:
        tmp = n % 10
        if tmp != 0: tich *= tmp
        n //= 10
    print(tich)